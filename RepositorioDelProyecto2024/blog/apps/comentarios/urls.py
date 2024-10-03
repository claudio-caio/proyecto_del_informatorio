from django.urls import path
from .views import AgregarComentarioView

app_name = 'comentarios'

urlpatterns = [
    path('comentarios/agregar/<int:articulo_id>/', AgregarComentarioView.as_view(), name='agregar_comentario'),
]
