from rest_framework.views import APIView
from rest_framework import permissions
from product.models import Products
from mypage.serializers import MyBookmarkListSerializer, MyProductListSerializer, MyOrderListSerializer
from rest_framework.response import Response
from rest_framework import status
from product.models import Products
from order.models import Orders
from rest_framework.generics import get_object_or_404


#회원 정보 확인 및 수정
class ProfileView(APIView):             

    def get(self, request):
        pass

    def put(self, request):
        pass

#bookmarklist/ 찜한 상품 리스트
class MyBookmarkView(APIView):         
    permission_classes=[permissions.IsAuthenticated]

    def get(self, request):
        bookmark_list = Products.objects.filter(bookmark=request.user.id)
        if bookmark_list:
            serializer = MyBookmarkListSerializer(bookmark_list, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"message":"잘못된 접근입니다!"}, status=status.HTTP_400_BAD_REQUEST)

#myproducts/ 내가 만든 상품 리스트
class MyProductsView(APIView):      
    def get(self, request):
        product = Products.objects.filter(user_id=request.user.id)
        serializer = MyProductListSerializer(product, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

#myorderlist/ 나의 주문 목록
class MyOrderlistView(APIView):      
    def get(self, request):
        product = Orders.objects.filter(user_id=request.user.id)
        serializer = MyOrderListSerializer(product, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
