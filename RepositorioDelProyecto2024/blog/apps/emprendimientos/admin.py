from django.contrib import admin
from .models import Categoria, Articulo

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')
    search_fields = ('nombre',)

class ArticuloAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'categoria')
    list_filter = ('categoria',)
    search_fields = ('titulo', 'contenido')

admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Articulo,ArticuloAdmin)