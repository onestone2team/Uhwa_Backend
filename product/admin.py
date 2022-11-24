from django.contrib import admin
from product.models import Categories, Products, Comments
# Register your models here.

admin.site.register(Categories)
admin.site.register(Products)
admin.site.register(Comments)