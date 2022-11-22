from . import views
from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('', views.ProductView.as_view(), name='product_view'),
    path('create/', views.ProductCreate.as_view(), name='product_create'),
    path('<int:product_id>/', views.ProductDetail.as_view(), name='product_detail'),
    path('<int:product_id>/comment/', views.ProductComment.as_view(), name='comment_create'),
    path('<int:product_id>/comment/<int:comment_id>/', views.CommentDetail.as_view(), name='comment_detail'),


]