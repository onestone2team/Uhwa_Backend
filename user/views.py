from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
# Create your views here.

class UserView(APIView):        #signup/ 회원가입

    def post(self, request):
        pass

class UserLogin(APIView):        #login/ 로그인
    
    def get(self, request):
        pass

    def post(self, request):
        pass

class UserDelete(APIView):      #delete/ 회원 탈퇴

    def delete(self, request):
        pass