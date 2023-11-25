from django.contrib import admin

from .models import Midia

class VisualNameMidia(admin.ModelAdmin):
  
  list_display = ('Id', 'Autor', 'Categoria', 'Publicada')
  list_display_links = ('Id', 'Autor', 'Categoria')
  search_field = ('Autor', 'Categoria')
  list_filter = ('Autor', 'Categoria')
  list_editable = ('Publicada',)
  list_per_page = 20

admin.site.register(Midia,VisualNameMidia)