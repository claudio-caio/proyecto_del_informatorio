from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Articulo, Categoria
from .forms import ArticuloForm

class ArticuloListView(ListView):
    model = Articulo
    template_name = 'emprendimientos/lista_articulos.html'
    context_object_name = 'articulos'

    def get_queryset(self):
        queryset = super().get_queryset()
        categoria_id = self.request.GET.get('categoria')  # Obtener el id de la categoría del query string
        if categoria_id:
            queryset = queryset.filter(categoria_id=categoria_id)  # Filtrar por categoría
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.all()  # Pasar todas las categorías al template
        return context
    
class ArticuloDetailView(DetailView):
    model = Articulo
    template_name = 'emprendimientos/detalle_articulo.html'
    context_object_name = 'articulo'

class ArticuloCreateView(CreateView):
    model = Articulo
    form_class = ArticuloForm
    template_name = 'emprendimientos/crear_articulo.html'
    success_url = reverse_lazy('emprendimientos:lista_articulos')  

class ArticuloUpdateView(UpdateView):
    model = Articulo
    form_class = ArticuloForm
    template_name = 'emprendimientos/editar_articulo.html'
    success_url = reverse_lazy('emprendimientos:lista_articulos')  

class ArticuloDeleteView(DeleteView):
    model = Articulo
    template_name = 'emprendimientos/eliminar_articulo.html'
    success_url = reverse_lazy('emprendimientos:lista_articulos')

