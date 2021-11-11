from django.contrib import admin
from django.urls import path, include
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', include_docs_urls(title='DDM')),
    path('admin/', admin.site.urls),
    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.jwt')),
    path('api/v1/', include('shops.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
