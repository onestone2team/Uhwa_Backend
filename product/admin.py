from django.contrib import admin
from product.models import Categories, Products, Comments,User_image
# Register your models here.

admin.site.register(Categories)
admin.site.register(Products)
admin.site.register(Comments)
admin.site.register(User_image)