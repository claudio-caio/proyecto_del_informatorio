from django.urls import path
from .views import AgregarComentarioView

app_name = 'comentarios'

urlpatterns = [
    path('articulos/<int:articulo_id>/comentarios/', AgregarComentarioView.as_view(), name='agregar_comentario'),
]
