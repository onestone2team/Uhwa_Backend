from rest_framework.views import APIView
from product.models import Products, Categories
from product.serializer import ProductsSerializer, CategorySerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from product.permissions import IsAdminOrAuthenticatedOrReadOnly
# Create your views here.

class ProductView(APIView):         # main 페이지 내 전체 데이터 불러오기

    def get(self, request):
        print(request.method)
        pagination = PageNumberPagination()
        pagination.page_size = 16
        pagination.page_query_param = "pages"
        products = Products.objects.all()
        p = pagination.paginate_queryset(queryset=products, request=request)
        serializer = ProductsSerializer(p, many=True)

        return Response({"data":serializer.data, "max_page":len(products)//16 +1}, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ProductsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data":serializer.data, "message":"생성이 완료되었습니다"}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductDetail(APIView):       # <int:product_id>/ 제품 상세 페이지

    def get(self, request):
        pass

    def post(self, request):
        pass

class ProductComment(APIView):      # 상세 페이지내 댓글 생성

    def post(self, request):
        pass

class CommentDetail(APIView):       # 댓글 수정 및 삭제 기능

    def put(self, request):
        pass

    def delete(self, request):
        pass

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