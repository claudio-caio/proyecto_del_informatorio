from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView,TemplateView
from django.urls import reverse_lazy
from .models import Articulo, Categoria
from django.db.models import Sum
from .forms import ArticuloForm
from apps.comentarios.models import Comentario
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.views.generic import ListView
from .models import Articulo, Categoria

class ArticuloListView(ListView):
    model = Articulo
    template_name = 'emprendimientos/lista_articulos.html'
    context_object_name = 'articulos'

    def get_queryset(self):
        queryset = super().get_queryset()
        categoria_id = self.request.GET.get('categoria')
        ordenar_por = self.request.GET.get('ordenar_por')  

        
        if categoria_id:
            queryset = queryset.filter(categoria_id=categoria_id)

        
        if ordenar_por == 'asc':
            queryset = queryset.order_by('visitas')  
        elif ordenar_por == 'desc':
            queryset = queryset.order_by('-visitas')  

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.all()
        return context

    
class ArticuloDetailView(DetailView):
    model = Articulo
    template_name = 'emprendimientos/detalle_articulo.html'
    context_object_name = 'articulo'

    def get_object(self):
        # Incrementar el contador de visitas
        articulo = super().get_object()
        articulo.visitas += 1
        articulo.save()
        return articulo

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
        return self.request.user == articulo.autor 
    
class PaginaPrincipalView(TemplateView):
    template_name = 'base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Sumar todas las visitas de los artículos
        total_visitas = Articulo.objects.aggregate(total_visitas=Sum('visitas'))['total_visitas'] or 0
        context['total_visitas'] = total_visitas
        return context