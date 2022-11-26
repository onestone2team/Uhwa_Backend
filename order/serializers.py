from order.models import Orders
from rest_framework import serializers
from product.serializers import ProductSerializer


class OrderListSerializer(serializers.ModelSerializer):
    product=ProductSerializer()
    class Meta:
        model = Orders
        fields = "__all__"


class AddOrderListSerializer(serializers.ModelSerializer):
    product = serializers.SerializerMethodField()
    
    def get_product(self,obj):
        return obj.product.category_id

    class Meta:
        model = Orders
        fields = ("price", "size", "count", "product")


class ChangeOrderStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = "__all__"

    def update(self, instance, validated_data):
        instance.order_status = validated_data.get('order_status', instance.order_status)
        instance.save()
        return instance