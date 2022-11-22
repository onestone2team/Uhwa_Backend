from . import views
from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import (
                                                TokenObtainPairView,
                                                TokenRefreshView,
                                            )


urlpatterns = [
    
    path('signup/', views.UserSignupView.as_view(), name='user_signup'),
    path('login/', TokenObtainPairView.as_view(), name='user_login'),
    path('login/refresh/', TokenRefreshView.as_view(), name='user_token_refresh'),
    path('delete/', views.UserDeleteView.as_view(), name='user_delete'),
    
]