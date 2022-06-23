from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.permissions import IsAuthenticatedOrReadOnly

urlpatterns = [
    path('', include_docs_urls(title='MYEyes', permission_classes=[IsAuthenticatedOrReadOnly,])),
    path('admin/', admin.site.urls),
    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.jwt')),
    path('api/v1/', include('shops.urls')),
    path('api/v1/', include('users.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
