from order.models import Orders
from rest_framework import serializers


class OrderListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = "__all__"


class AddOrderListSerializer(serializers.ModelSerializer):
    class Meta:

        model = Orders
        fields = ("price", "size", "count")


class ChangeOrderStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = "__all__"

    def update(self, instance, validated_data):
        instance.order_status = validated_data.get('order_status', instance.order_status)
        instance.save()
        return instance