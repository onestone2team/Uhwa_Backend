from rest_framework import serializers
from product.models import Products


class BookmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ("id", "user_id", "hide_option", "image")



class MyProductListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Products
        fields = ("id", "user_id", "hide_option", "image")

class ProfileMyOrderlistSerializer(serializers.ModelSerializer):

    class Meta:
        model = Products
        fields = "__all__"
