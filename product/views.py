from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from product.models import Comments
from product.seriailzers import CommentsSerializer

#Create your views here.

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
    def post(self, request, product_id,format=None):
     serializer = CommentsSerializer(data= request.data)
     if serializer.is_valid():
        serializer.save()
        return Response({"message": "해당 글이 생성되었습니다.", "data":"serializer.data"} , status=status.HTTP_200_OK )
     else:
       return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

class CommentDetail(APIView):       # 댓글 수정 및 삭제 기능
    def put(self, request, product_id, comment_id):
        comment = get_object_or_404(Comments, id=comment_id)
        serializer = CommentsSerializer(comment, data = request.data)
        if serializer.is_valid():
          serializer.save()  
          return Response({"message":"해당 글이 수정되었습니다.","data":"serializer.data"}, status=status.HTTP_201_CREATED)

    def delete(self, request, product_id, comment_id):
        comment = get_object_or_404(Comments, id=comment_id)
        comment.delete()
        return Response({"message":"해당 글이 삭제되었습니다."}, status=status.HTTP_204_NO_CONTENT)
