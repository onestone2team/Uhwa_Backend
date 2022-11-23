from rest_framework import serializers
from rest_framework import status
from product.models import Products


class BookmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = "__all__"



class MyProductListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Products
        fields = "__all__"

