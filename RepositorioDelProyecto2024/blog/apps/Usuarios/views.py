from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView,TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from .forms import FormularioRegistroUsuario
from django.contrib.auth.mixins import LoginRequiredMixin


class RegistroUsuario(CreateView):
    template_name = 'usuarios/registro.html'
    form_class = FormularioRegistroUsuario
    success_url = reverse_lazy('index')

class InicioSesion(LoginView):
    template_name = 'usuarios/login.html'

class CerrarSesion(LogoutView):
    template_name = 'usuarios/logout.html'
    next_page = reverse_lazy('index')

class PerfilView(LoginRequiredMixin, TemplateView):
    template_name = 'usuarios/perfil.html'