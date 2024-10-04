from django.contrib import admin
from django.urls import path, include
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('contacto', views.Contacto, name='contacto'),
    path('nosotros', views.Nosotros, name='nosotros'),
    path('emprendimientos/', include(('apps.emprendimientos.urls', 'emprendimientos'), namespace='emprendimientos')),
    path('comentarios/', include(('apps.comentarios.urls', 'comentarios'), namespace='comentarios')),
    path('Usuarios/', include(('apps.Usuarios.urls', 'Usuarios'), namespace='Usuarios')),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

