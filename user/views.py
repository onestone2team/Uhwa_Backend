from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from user.serializers import UserSerializer,CustomedUserSerializer
from .models import Users
# Create your views here.

#signup/ 회원가입
class UserSignupView(APIView):        
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"message":"회원가입 성공!"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message":"다시 시도해주세요"}, status=status.HTTP_400_BAD_REQUEST)

#login/ 로그인
class UserLoginView(TokenObtainPairView):        
    serializer_class = CustomedUserSerializer

#delete/ 회원 탈퇴
class UserDeleteView(APIView):      
    def delete(self, request):
        print(request.user)
        user = Users.objects.get(id=request.user.id)
        if user:
            user.delete()
            return Response({"message": "계정이 삭제되었습니다."}, status=status.HTTP_200_OK)
        return Response({"message": "잘못된 요청입니다. 다시 시도해주세요."}, status=status.HTTP_400_BAD_REQUEST)