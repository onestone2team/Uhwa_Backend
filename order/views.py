from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from order.models import Orders
from order.serializers import OrderListSerializer, AddOrderListSerializer, ChangeOrderStatusSerializer
from rest_framework import permissions


#list/ 주문 목록 보기
class OrderList(APIView):
    def get(self, request):
        orders = Orders.objects.filter(user_id=request.user.id)
        serializer = OrderListSerializer(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

#list/ 주문 목록 추가
class AddOrderList(APIView):
    def post(self, request, product_id):
        # product = Products.objects.get(id=product_id)
        serializer = AddOrderListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(product_id=product_id, user_id=request.user.id)
            return Response({"message":"주문목록에 추가되었습니다!", "data":serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ChangeOrderStatus(APIView):
    #list/<int:order_id>/ 주문 상태 변경
    permission_classes=[permissions.IsAdminUser]

    def get(self, request):
        orders = Orders.objects.all()
        serializer = OrderListSerializer(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, order_id):
        order = Orders.objects.get(id=order_id)
        serializer = ChangeOrderStatusSerializer(order, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)