from django.contrib import admin

from cursos.models import Curso

# Register your models here.

class ListandoCursos(admin.ModelAdmin):
    
    list_display = ('nome', 'id')

    def get_nome(self, obj):
        return obj.nome
    
    get_nome.short_description = 'Nome do curso'  #Renames column head

admin.site.register(Curso, ListandoCursos)