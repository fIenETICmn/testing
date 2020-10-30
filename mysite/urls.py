from django.contrib import admin
from django.urls import path, include
from .routers import router


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('', include('django.contrib.auth.urls')),
    path('api/',include(router.urls)),
]