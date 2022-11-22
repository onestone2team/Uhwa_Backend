from . import views
from django.contrib import admin
from django.urls import path


urlpatterns = [
    
    path('list/', views.OrderList.as_view(), name='order_list'),
    path('list/<int:order_id>/', views.OrderChangeStatus.as_view(), name='order_status'),

]