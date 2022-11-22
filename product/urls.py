from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.ProductView.as_view(), name='product_view'),
    path('create/', views.ProductView.as_view(), name='product_create'),
    path('<int:product_id>/', views.ProductDetail.as_view(), name='product_detail'),
    path('<int:product_id>/comment/', views.ProductComment.as_view(), name='comment_create'),
    path('<int:product_id>/comment/<int:comment_id>/', views.CommentDetail.as_view(), name='comment_detail'),
    path('category/', views.CategoriView.as_view(), name="category_view"),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)