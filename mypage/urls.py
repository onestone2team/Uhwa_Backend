from . import views
from django.urls import path


urlpatterns = [

    path('', views.ProfileView.as_view(), name='profile_view'),
    path('bookmarklist/', views.ProfileBookmark.as_view(), name='profile_bookmark'),
    path('myproducts/', views.ProfileMyProducts.as_view(), name='profile_product'),
    path('myorderlist/', views.ProfileMyOrderlis.as_view(), name='profile_order'),

]