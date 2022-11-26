from rest_framework import serializers
from product.models import Products
from order.models import Orders
from product.serializers import ProductSerializer

class MyBookmarkListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ("id", "user_id", "hide_option", "image")

class MyProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ("id", "user_id", "hide_option", "image")

class MyOrderListSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = Orders
        fields = ("user", "product", "count", "size", "product", "price", "order_status")

