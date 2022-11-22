from . import views
from django.contrib import admin
from django.urls import path


urlpatterns = [

    path('signup/', views.UserView.as_view(), name='user_signip'),
    path('login/', views.UserLogin.as_view(), name='user_login'),
    path('delete/', views.UserDelete.as_view(), name='user_delete'),

]