from rest_framework import serializers
from product.models import Products, Categories


def hide_option_validator():
    pass


class ProductSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    def get_user(self, obj):
        return obj.user.email

    class Meta:
        model = Products
        fields = "__all__"

class ProductsDetailSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    comment_set = serializers.SerializerMethodField()

    def get_user(self, obj):
        return obj.user.email

    class Meta:
        model = Products
        fields = ("user", "image", "bookmark","comment_set")

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