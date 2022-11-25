from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from user.serializers import UserSerializer, CustomedUserSerializer, UserInactiveSerializer
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

#delete/ 회원 탈퇴 및 비활성화
class UserDeleteView(APIView):
    def put(self,request):
        user = Users.objects.get(id=request.user.id)
        user_inactive = dict()
        for key, value in request.data.items():
            if value:
                user_inactive.update({key:value})
        inactive_serializer = UserInactiveSerializer(user, data = user_inactive, partial=True)
        if inactive_serializer.is_valid(raise_exception=True):
            inactive_serializer.save()
            return Response({"data":inactive_serializer.data,"message":"계정이 비활성화 되었습니다."}, status=status.HTTP_200_OK)
        return Response({"message":"저장되지 않았습니다. 다시 시도해주세요"}, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request):
        user = Users.objects.get(id=request.user.id)
        if user:
            user.delete()
            return Response({"message": "계정이 삭제되었습니다."}, status=status.HTTP_200_OK)
        return Response({"message": "잘못된 요청입니다. 다시 시도해주세요."}, status=status.HTTP_400_BAD_REQUEST)