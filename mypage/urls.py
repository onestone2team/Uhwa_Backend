from . import views
from django.contrib import admin
from django.urls import path


urlpatterns = [

    path('', views.ProfileView.as_view(), name='profile_view'),
    path('bookmarklist/', views.ProfileBookmark.as_view(), name='profile_bookmark'),
    path('myproducts/', views.ProfileMyProducts.as_view(), name='profile_product'),
    path('myorderlist/', views.ProfileMyOrderlist.as_view(), name='profile_order'),
    
]