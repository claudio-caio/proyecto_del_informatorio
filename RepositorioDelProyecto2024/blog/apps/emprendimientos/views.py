from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Articulo, Categoria
from .forms import ArticuloForm
from apps.comentarios.models import Comentario
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class ArticuloListView(ListView):
    model = Articulo
    template_name = 'emprendimientos/lista_articulos.html'
    context_object_name = 'articulos'

    def get_queryset(self):
        queryset = super().get_queryset()
        categoria_id = self.request.GET.get('categoria')  
        if categoria_id:
            queryset = queryset.filter(categoria_id=categoria_id)  
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.all()  
        return context
    
class ArticuloDetailView(DetailView):
    model = Articulo
    template_name = 'emprendimientos/detalle_articulo.html'
    context_object_name = 'articulo'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comentarios'] = Comentario.objects.filter(articulo=self.object)
        return context

    def post(self, request, *args, **kwargs):
        articulo = self.get_object()
        contenido = request.POST.get('contenido')  
        if contenido:
            Comentario.objects.create(
                contenido=contenido,
                articulo=articulo,
                autor=request.user
            )
        return self.get(request, *args, **kwargs)

class ArticuloCreateView(LoginRequiredMixin, CreateView):
    model = Articulo
    form_class = ArticuloForm
    template_name = 'emprendimientos/crear_articulo.html'
    success_url = reverse_lazy('emprendimientos:lista_articulos')  

    def form_valid(self, form):
        form.instance.autor = self.request.user  # Asignar el autor al usuario logueado
        return super().form_valid(form)
    

class ArticuloUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Articulo
    form_class = ArticuloForm
    template_name = 'emprendimientos/editar_articulo.html'
    success_url = reverse_lazy('emprendimientos:lista_articulos')

    def test_func(self):
        articulo = self.get_object()
        return self.request.user == articulo.autor  # Solo el autor puede editar

class ArticuloDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Articulo
    template_name = 'emprendimientos/eliminar_articulo.html'
    success_url = reverse_lazy('emprendimientos:lista_articulos')

    def test_func(self):
        articulo = self.get_object()
        return self.request.user == articulo.autor  # Solo el autor puede eliminar