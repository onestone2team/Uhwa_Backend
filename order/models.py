from django.db import models
from product.models import Users, Products
# Create your models here.

class Orders(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    price = models.IntegerField()
    size = models.CharField(max_length=5)
    count = models.IntegerField()
    created_at = models.DateField(auto_now_add = True)
    order_status = models.IntegerField(default=0, blank=True)
