from django.urls import path
from .views import AgregarComentarioView,ComentarioDeleteView,ComentarioUpdateView

app_name = 'comentarios'

urlpatterns = [
    path('comentarios/agregar/<int:articulo_id>/', AgregarComentarioView.as_view(), name='agregar_comentario'),
    path('editar/<int:pk>/', ComentarioUpdateView.as_view(), name='editar_comentario'),
    path('eliminar/<int:pk>/', ComentarioDeleteView.as_view(), name='eliminar_comentario'),
]
