from . import views
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [

    path('signup/', views.UserSignupView.as_view(), name='user_signup'),
    path('login/', views.UserLoginView.as_view(), name='user_login'),
    path('login/refresh/', TokenRefreshView.as_view(), name='user_token_refresh'),
    path('delete/', views.UserDeleteView.as_view(), name='user_delete'),

]