from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import Comentario
from apps.emprendimientos.models import Articulo

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
