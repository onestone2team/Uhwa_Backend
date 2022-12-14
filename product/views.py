from rest_framework.views import APIView
from product.models import Products, Comments, Categories, MachineLearning
from product.serializers import (ProductCreateSerializer, ProductDetailSerializer, ProductSerializer, CategorySerializer, 
                                 CommentsSerializer, CommentCreateSerializer,
                                 MachineLearningSerializer)
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework.generics import get_object_or_404
from product.deeplearning import get_result_shirt,model
import cv2
import base64
from django.db.models import Q
from rest_framework.pagination import PageNumberPagination
from product.permissions import IsAdminOrAuthenticatedOrReadOnly, DeletePermissition





# main 페이지 내 전체 데이터 불러오기
class ProductView(APIView):
    def get(self, request):
        pagination = PageNumberPagination()
        pagination.page_size = 9
        pagination.page_query_param = "page"
        products = Products.objects.filter(hide_option=0).order_by("-created_at")

        p = pagination.paginate_queryset(queryset=products, request=request)
        serializer = ProductSerializer(p, many=True)
        return Response({"data": serializer.data, "max_page": len(products)//9 + 1}, status=status.HTTP_200_OK)

# 머신러닝
# 상품 생성
class ProductCreateView(APIView):
    permission_classes=[permissions.IsAuthenticated]
    def post(self, request):
        serializer = ProductCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response({"data":serializer.data,"message":"이미지전송 성공"}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 상품 삭제(관리자 기능)
class ProductDeleteView(APIView):
    permission_classes = (DeletePermissition,)

    def delete(self, reqeust, products_id):
        product = Products.objects.get(id=products_id)
        product.delete()
        return Response({"message": "삭제되었습니다!"}, status=status.HTTP_200_OK)

# <int:product_id>/ 제품 상세 페이지
class ProductDetailView(APIView):
    def get(self, request, product_id):
        product = get_object_or_404(Products, id=product_id)
        serializer = ProductDetailSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductCreateView(APIView):
    permission_classes=[permissions.IsAuthenticated]

    def post(self, request):
            serializer = ProductCreateSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(user_id=request.user.id)
                return Response({"data": serializer.data, "message": "생성이 완료되었습니다"}, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MachineLearningView(APIView):

    def post(self, request):
        serializer = MachineLearningSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            img_url=model(serializer.data["image"], serializer.data["model"])
            get_result_shirt(img_url,serializer.data["category"])
            return Response({"data":serializer.data, "message":"이미지전송 성공"}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductComment(APIView):      # 상세 페이지내 댓글 생성
    def post(self, request, product_id, format=None):
        comment = Comments.objects.filter(Q(user_id=request.user.id) & Q(product_id=product_id)).order_by("-created_at")
        if comment.count() < 1:
            serializer = CommentCreateSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(product_id=product_id, user=request.user)
                return Response({"message": "해당 글이 생성되었습니다.", "data": serializer.data}, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"message":"댓글은 하나만 등록 할 수 있습니다!"}, status=status.HTTP_400_BAD_REQUEST)

# 댓글 수정 및 삭제 기능
class CommentDetailView(APIView):
    def put(self, request, product_id, comment_id):
        comment = get_object_or_404(Comments, id=comment_id)
        serializer = CommentCreateSerializer(comment, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "해당 글이 수정되었습니다.", "data": serializer.data}, status=status.HTTP_201_CREATED)
        else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, product_id, comment_id):
        comment = Comments.objects.filter(Q(user_id=request.user.id) & Q(id=comment_id))
        comment.delete()
        return Response({"message": "해당 글이 삭제되었습니다."}, status=status.HTTP_204_NO_CONTENT)

# 상세페이지 북마크
class ProductBookmarkView(APIView):
    permission_classes=[permissions.IsAuthenticated]

    def post(self, request, product_id):
        bookmark_list = get_object_or_404(Products, id=product_id)
        if request.user in bookmark_list.bookmark.all():
            bookmark_list.bookmark.remove(request.user)
            return Response({"message":"북마크에 삭제되었습니다"}, status=status.HTTP_200_OK)
        else:
            bookmark_list.bookmark.add(request.user)
            return Response({"message":"북마크에 추가하였습니다"}, status=status.HTTP_202_ACCEPTED)

# 상품 카테고리
class CategoryView(APIView):
    permission_classes = (IsAdminOrAuthenticatedOrReadOnly, )

    def get(self, request):
        categories = Categories.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ShirtView(APIView):

    def get(self, request):
        pagination = PageNumberPagination()
        pagination.page_size = 9
        pagination.page_query_param = "page"
        products = Products.objects.filter(Q(category_id=1) & Q(hide_option=0)).order_by("-created_at")

        p = pagination.paginate_queryset(queryset=products, request=request)
        serializer = ProductSerializer(p, many=True)
        return Response({"data": serializer.data, "max_page": len(products)//9 + 1}, status=status.HTTP_200_OK)

class CapView(APIView):

    def get(self, request):
        pagination = PageNumberPagination()
        pagination.page_size = 9
        pagination.page_query_param = "page"
        products = Products.objects.filter(Q(category_id=2) & Q(hide_option=0)).order_by("-created_at")

        p = pagination.paginate_queryset(queryset=products, request=request)
        serializer = ProductSerializer(p, many=True)
        return Response({"data": serializer.data, "max_page": len(products)//9 + 1}, status=status.HTTP_200_OK)

class HoodView(APIView):

    def get(self, request):
        pagination = PageNumberPagination()
        pagination.page_size = 9
        pagination.page_query_param = "page"
        products = Products.objects.filter(Q(category_id=3) & Q(hide_option=0)).order_by("-created_at")

        p = pagination.paginate_queryset(queryset=products, request=request)
        serializer = ProductSerializer(p, many=True)
        return Response({"data": serializer.data, "max_page": len(products)//9 + 1}, status=status.HTTP_200_OK)