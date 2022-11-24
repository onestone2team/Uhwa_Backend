from . import views
from django.urls import path


urlpatterns = [

    path('', views.ProfileView.as_view(), name='profile_view'),
    path('bookmarklist/', views.MyBookmarkView.as_view(), name='profile_bookmark'),
    path('myproducts/', views.MyProductsView.as_view(), name='profile_product'),
    path('myorderlist/', views.MyOrderlistView.as_view(), name='profile_order'),

]