from rest_framework import serializers
from rest_framework import status
from product.models import Products, Categories


def hide_option_validator():
    pass


class ProductsSerializer(serializers.ModelSerializer):
    product_user = serializers.SerializerMethodField()
    
    def get_product_user(self, obj):
        return self.product_user.user
    class Meta:
        model = Products
        fields = "__all__"

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Categories
        fields = "__all__"