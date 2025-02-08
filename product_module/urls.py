from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductListView.as_view(), name='product_list'),
    path('cat/<cat>/', views.ProductListView.as_view(), name='product_category_list'),
    path('brand/<brand>/', views.ProductListView.as_view(), name='product_list_by_brand'),
    path('product_favorite', views.AddProductFavorite.as_view(), name='product_favorite'),
    path('<slug:slug>', views.ProductDetailView.as_view(), name='product_detail')
]
