from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Comentario
from apps.emprendimientos.models import Articulo
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect


class AgregarComentarioView(CreateView):
    model = Comentario
    fields = ['contenido']
    template_name = 'comentarios/agregar_comentario.html'

    def form_valid(self, form):
        form.instance.autor = self.request.user  # Asigna el usuario actual como autor
        form.instance.articulo = Articulo.objects.get(id=self.kwargs['articulo_id'])  # Asigna el artículo al comentario
        return super().form_valid(form)

    def get_success_url(self):
        # Redirigir a la vista de detalle del artículo después de agregar el comentario
        return reverse_lazy('emprendimientos:detalle_articulo', kwargs={'pk': self.kwargs['articulo_id']})
    
class ComentarioUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comentario
    fields = ['contenido']  # Solo editamos el contenido
    template_name = 'comentarios/editar_comentario.html'

    def test_func(self):
        comentario = self.get_object()
        return self.request.user == comentario.autor  # Solo el autor puede editar el comentario

    def get_success_url(self):
        return reverse_lazy('emprendimientos:detalle_articulo', kwargs={'pk': self.object.articulo.pk})


class ComentarioDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comentario
    template_name = 'comentarios/eliminar_comentario.html'

    def test_func(self):
        comentario = self.get_object()
        return self.request.user == comentario.autor  # Solo el autor puede eliminar el comentario

    def get_success_url(self):
        return reverse_lazy('emprendimientos:detalle_articulo', kwargs={'pk': self.object.articulo.pk})