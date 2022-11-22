from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from user.serializers import UserSerializer,CustomedUserSerializer
# Create your views here.

class UserSignupView(APIView):        #signup/ 회원가입
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"message":"회원가입 성공!"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message":"다시 시도해주세요"}, status=status.HTTP_400_BAD_REQUEST)

# class UserLoginView(APIView):        #login/ 로그인
    
#     def get(self, request):
#         pass

#     def post(self, request):
#         pass

class UserLogoutView(APIView):
    def post(self, request):
        request.user.auth_token.delete()
        return Response({"message": "로그아웃되었습니다."}, status=status.HTTP_200_OK)

class UserDeleteView(APIView):      #delete/ 회원 탈퇴
    def delete(self, request):
        pass