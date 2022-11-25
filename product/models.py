from django.db import models
from user.models import Users
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Categories(models.Model):
    category_name = models.CharField(max_length=50)
    category_image = models.ImageField()
    category_price = models.IntegerField()

    def __str__(self):
        return str(self.category_name)

class Products(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='%y/%m/')
    hide_option = models.BooleanField(default=False)
    bookmark = models.ManyToManyField(Users, related_name = 'add_bookmark', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

class Comments(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    product = models.ForeignKey(Products,null=True,blank=True, on_delete=models.CASCADE)
    comment = models.TextField()
    grade = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    created_at = models.DateTimeField(auto_now_add = True)
    update_at = models.DateTimeField(auto_now = True)

class User_image(models.Model):
    user_image=models.ImageField(upload_to='%y/%m/')
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, blank=True, null=True)
