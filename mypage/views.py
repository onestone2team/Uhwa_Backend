from django.shortcuts import render
from rest_framework.views import APIView

# Create your views here.
class ProfileView(APIView):             #회원 정보 확인 및 수정

    def get(self, request):
        pass

    def put(self, request):
        pass

class ProfileBookmark(APIView):         #bookmarklist/ 찜한 상품 리스트

    def get(self, request):
        pass

class ProfileMyProducts(APIView):       #myproducts/ 내가 만든 상품 리스트

    def get(self, request):
        pass

class ProfileMyOrderlist(APIView):      #myorderlist/ 나의 주문 목록

    def get(self, request):
        pass
