from rest_framework.views import APIView
from product.models import Products, Categories,Comments
from product.serializer import ProductsSerializer, CategorySerializer, ProductsCreateSerializer,CommentsSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from product.permissions import IsAdminOrAuthenticatedOrReadOnly, DeletePermissition
from rest_framework.generics import get_object_or_404
import cv2
import base64

# Create your views here.


class ProductView(APIView):         # main 페이지 내 전체 데이터 불러오기

    def get(self, request):

        pagination = PageNumberPagination()
        pagination.page_size = 16
        pagination.page_query_param = "pages"
        products = Products.objects.all()
        p = pagination.paginate_queryset(queryset=products, request=request)
        serializer = ProductsSerializer(p, many=True)
        return Response({"data": serializer.data, "max_page": len(products)//16 + 1}, status=status.HTTP_200_OK)


class DeleteProductView(APIView):
    permission_classes = (DeletePermissition,)

    def delete(self, reqeust, products_id):
        product = Products.objects.get(id=products_id)
        product.delete()
        return Response({"message": "삭제되었습니다!"}, status=status.HTTP_200_OK)


class ProductCreateView(APIView):
    # permission_classes=[permissions.IsAuthenticated]
    def post(self, request):
        serializer = ProductsCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response({"data": serializer.data, "message": "생성이 완료되었습니다"}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MachineRunningView(APIView):

    def post(self, request):
        print(request.data)
        print(request.data["image"])
        img = cv2.imread(f'{request.data["image"]}')
        print(img)
        jpg_img = cv2.imencode('.jpg', img)
        b64_string = base64.b64encode(jpg_img[1]).decode('utf-8')
        return Response({"image": b64_string})


class ProductDetail(APIView):       # <int:product_id>/ 제품 상세 페이지

    def get(self, request):
        pass

    def post(self, request):
        pass


class ProductComment(APIView):      # 상세 페이지내 댓글 생성
    def post(self, request, product_id, format=None):
        serializer = CommentsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "해당 글이 생성되었습니다.", "data": "serializer.data"}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentDetail(APIView):       # 댓글 수정 및 삭제 기능
    def put(self, request, product_id, comment_id):
        comment = get_object_or_404(Comments, id=comment_id)
        serializer = CommentsSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "해당 글이 수정되었습니다.", "data": "serializer.data"}, status=status.HTTP_201_CREATED)

    def delete(self, request, product_id, comment_id):
        comment = get_object_or_404(Comments, id=comment_id)
        comment.delete()
        return Response({"message": "해당 글이 삭제되었습니다."}, status=status.HTTP_204_NO_CONTENT)


class CategoriView(APIView):
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
            return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)


class Bookmarkhandle(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, product_id):
        bookmark_list = get_object_or_404(Products, id=product_id)
        if request.user in bookmark_list.bookmark.all():
            bookmark_list.bookmark.remove(request.user)
            return Response({"message": "북마크에 삭제되었습니다"}, status=status.HTTP_200_OK)
        else:
            bookmark_list.bookmark.add(request.user)
            return Response({"message":"북마크에 추가하였습니다"}, status=status.HTTP_202_ACCEPTED)
