from rest_framework import serializers
from user.serializers import UserCommentSerializer
from product.models import Products, Categories, User_image, Comments, MachineLearning

import cv2
import base64

def hide_option_validator():
    pass

class ProductSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    def get_user(self, obj):
        return obj.user.email

    class Meta:
        model = Products
        fields = "__all__"


class ProductCreateSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    def get_user(self, obj):
        return obj.user.email

    class Meta:
        model = Products
        fields = ("user", "image", "category", "hide_option")


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Categories
        fields = "__all__"

class UserimagesaveSerializer(serializers.ModelSerializer):

    class Meta:
        model = User_image
        fields = "__all__"

class CommentsSerializer(serializers.ModelSerializer):
    user=UserCommentSerializer()
    class Meta:
        model = Comments
        fields = ("id", "comment", "grade", "user", "created_at")
    
class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ("comment", "grade",)
    
class ProductDetailSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    comments_set = CommentsSerializer(many=True)

    def get_user(self, obj):
        return obj.user.email

    class Meta:
        model = Products
        fields = ( "user", "image", "bookmark", "comments_set")

class MachineLearningSerializer(serializers.ModelSerializer):
    class Meta:
        model = MachineLearning
        fields = ("model", "category", "image")

    # def create(self, validated_data):
    #     print()
    #     print(validated_data)
    #     img = cv2.imread(validated_data.image)
    #     jpg_img = cv2.imencode('.jpg', img)
    #     b64_string = base64.b64encode(jpg_img[1]).decode('utf-8')
    #     print(b64_string)
    #     return "안돼에에ㅔㅔ"

