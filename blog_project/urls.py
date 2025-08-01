# blog_project/urls.py

from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from posts import views

from django.conf import settings
from django.conf.urls.static import static

# Setup the API router
router = routers.DefaultRouter()
router.register(r'posts', views.PostApiViewSet, basename='post')

urlpatterns = [
    # Main project URLs
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    
    # ADD THIS LINE: It tells Django to look for URLs in your 'posts' app
    path('', include('posts.urls')),

    # API URLs
    path('api/', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)