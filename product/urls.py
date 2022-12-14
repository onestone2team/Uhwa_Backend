from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.ProductView.as_view(), name='product_view'),
    path('<int:products_id>/', views.ProductDeleteView.as_view(), name='product_delete_view'),
    path('create/', views.ProductCreateView.as_view(), name='product_create'),
    path('machinelearning/', views.MachineLearningView.as_view(), name='product_machinelearmimg'),
    path('<int:product_id>/detail/', views.ProductDetailView.as_view(), name='product_detail'),
    path('<int:product_id>/bookmark/', views.ProductBookmarkView.as_view(), name='product_bookmark'),
    path('<int:product_id>/comment/', views.ProductComment.as_view(), name='comment_create'),
    path('<int:product_id>/comment/<int:comment_id>/', views.CommentDetailView.as_view(), name='comment_detail'),
    path('category/', views.CategoryView.as_view(), name="category_view"),
    path('shirt/', views.ShirtView.as_view(), name="shirt_view"),
    path('cap/', views.CapView.as_view(), name="cap_view"),
    path('hood/', views.HoodView.as_view(), name="hood_view"),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)