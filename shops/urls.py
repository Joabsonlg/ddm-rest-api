from django.urls import path, include
from . import views

urlpatterns = [
    path('shops/', views.getAllShops),
    path('shops/save/', views.createShop),
    path('shops/<slug:slug>/', views.getShop),
    path('shops/user/<int:id>/', views.getShopByUser),
    path('shops/<slug:slug>/update/', views.updateShop),
    path('shops/<slug:slug>/delete/', views.deleteShop),
    path('shops/<slug:slug>/products/', views.getProductsFromShop),
    path('products/', views.getAllProducts),
    path('products/save/', views.createProduct),
    path('products/<slug:slug>/', views.getProduct),
    path('products/<slug:slug>/update/', views.updateProduct),
    path('products/<slug:slug>/delete/', views.deleteProduct),
    path('products/<slug:slug>/qr-code/', views.getQRCode),
    path('products/<slug:slug>/qr-code/download', views.getQRCodePdf),
    path('categories/', views.getAllCategories),
    path('categories/save/', views.createCategory),
    path('categories/<slug:slug>/', views.getCategory),
    path('categories/<slug:slug>/update/', views.updateCategory),
    path('categories/<slug:slug>/delete/', views.deleteCategory)
]
