from . import views
from django.contrib import admin
from django.urls import path


urlpatterns = [

    path('list/', views.OrderList.as_view(), name='order_list'),
    path('list/<int:product_id>/', views.AddOrderList.as_view(), name='order_list'),
    path('list/admin/<int:order_id>/', views.ChangeOrderStatus.as_view(), name='order_status'),
    path('list/admin/', views.ChangeOrderStatus.as_view(), name='order_status'),

]