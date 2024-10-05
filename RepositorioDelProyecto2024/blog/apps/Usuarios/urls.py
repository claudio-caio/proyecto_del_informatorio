from django.urls import path
from . import views

app_name = 'usuarios'

urlpatterns = [
    path('Registro/', views.RegistroUsuario.as_view(), name='registro_usuario'),
    path('Login/', views.InicioSesion.as_view(), name='login'),
    path('Logout/', views.CerrarSesion.as_view(), name='logout'),
    path('Perfil/', views.PerfilView.as_view(), name='perfil'),
]
