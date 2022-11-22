from django.shortcuts import render
from rest_framework.views import APIView

# Create your views here.

class OrderList(APIView):               #list/ 주문 목록 보기

    def get(self, request):
        pass

class OrderChangeStatus(APIView):       #list/<int:order_id>/ 주문 상태 변경

    def put(self, request):
        pass