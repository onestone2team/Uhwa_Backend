from rest_framework import serializers
from product.models import Products, Categories,User_image,Comments


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
        fields = ("user", "image")

class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Categories
        fields = "__all__"

class UserimagesaveSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User_image
        fields = "__all__"

class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = "__all__"