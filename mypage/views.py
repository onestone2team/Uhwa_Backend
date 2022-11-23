from rest_framework.views import APIView
from rest_framework import permissions
from product.models import Products
from mypage.serializer import BookmarkSerializer, MyProductListSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404
from product.models import Products
from order.models import Orders
# Create your views here.
class ProfileView(APIView):             #회원 정보 확인 및 수정

    def get(self, request):
        pass

    def put(self, request):
        pass

class ProfileBookmark(APIView):         #bookmarklist/ 찜한 상품 리스트
    permission_classes=[permissions.IsAuthenticated]

    def get(self, request):
        bookmark_list = Products.objects.filter(bookmark=request.user.id)
        if bookmark_list:
            serializer = BookmarkSerializer(bookmark_list, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"message":"잘못된 접근입니다!"}, status=status.HTTP_400_BAD_REQUEST)


class ProfileMyProducts(APIView):       #myproducts/ 내가 만든 상품 리스트

    def get(self, request):
        product = Products.objects.filter(id=request.user.id)
        serializer = MyProductListSerializer(product, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ProfileMyOrderlist(APIView):      #myorderlist/ 나의 주문 목록

    def get(self, request):
        product = Orders.objects.filter(id=request.user)
