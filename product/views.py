from django.shortcuts import render
from rest_framework.views import APIView
# Create your views here.

class ProductView(APIView):         # main 페이지 내 전체 데이터 불러오기

    def get(self, request):
        pass

class ProductCreate(APIView):       # create/ 제품 생성

    def post(self, request):
        pass

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
