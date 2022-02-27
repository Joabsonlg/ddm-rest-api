from django.urls import path

from .views import ShopViewSet, CategoryViewSet, ProductViewSet

urlpatterns = [
    path('shops', ShopViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('shops/<slug:slug>', ShopViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
    path('shops/user/<int:user_id>', ShopViewSet.as_view({
        'get': 'retrieve_by_user'
    })),
    path('shops/<slug:slug>/products', ShopViewSet.as_view({
        'get': 'retrieve_products'
    })),
    path('products', ProductViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('products/<slug:slug>', ProductViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
    path('products/<slug:slug>/qr-code-png', ProductViewSet.as_view({
        'get': 'retrieve_qr_code_png'
    })),
    path('products/<slug:slug>/qr-code-pdf', ProductViewSet.as_view({
        'get': 'retrieve_qr_code_pdf'
    })),
    path('categories', CategoryViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('categories/<slug:slug>', CategoryViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
]
