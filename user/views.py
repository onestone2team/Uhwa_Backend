from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from user.serializers import UserSerializer,CustomedUserSerializer,UserProfileSerializer
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
        user = Users.objects.get(id=request.user.id)
        if user:
            user.delete()
            return Response({"message": "계정이 삭제되었습니다."}, status=status.HTTP_200_OK)
        return Response({"message": "잘못된 요청입니다. 다시 시도해주세요."}, status=status.HTTP_400_BAD_REQUEST)

# 프로필 조회 및 수정
class UserProfileView(APIView):
    def get(self, request):
        profile = Users.objects.get(id=request.user.id)
        serializer = UserProfileSerializer(profile)
        return Response(serializer.data)
    def put(self,request):
        profile=Users.objects.get(id=request.user.id)
        profile_serializer = UserProfileSerializer(profile, data=request.data, partial=True)
        if profile_serializer.is_valid(raise_exception=True):
            profile_serializer.save()
            return Response({"data":profile_serializer.data,"message":"프로필 수정 완료"}, status=status.HTTP_201_CREATED)
        return Response({"message":"저장되지 않았습니다. 다시 시도해주세요"}, status=status.HTTP_400_BAD_REQUEST)
        
