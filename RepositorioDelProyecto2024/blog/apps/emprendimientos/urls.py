from django.urls import path,include
from .views import ArticuloListView, ArticuloDetailView, ArticuloCreateView, ArticuloUpdateView, ArticuloDeleteView,PaginaPrincipalView
from .views import ArticuloDetailView

app_name = 'emprendimientos'  

urlpatterns = [
    path('', ArticuloListView.as_view(), name='lista_articulos'),
    path('', PaginaPrincipalView.as_view(), name='pagina_principal'),
    path('detalle/<int:pk>/', ArticuloDetailView.as_view(), name='detalle_articulo'),
    path('crear/', ArticuloCreateView.as_view(), name='crear_articulo'),
    path('editar/<int:pk>/', ArticuloUpdateView.as_view(), name='editar_articulo'),
    path('eliminar/<int:pk>/', ArticuloDeleteView.as_view(), name='eliminar_articulo'),
    path('comentarios/', include('apps.comentarios.urls')),
]
