from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from hola.views import def_hola, def_login


urlpatterns = [
    path('admin/', admin.site.urls),
    path('hola/', def_hola),
    path('login/', def_login),
    path('articulos/', include('hola.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
