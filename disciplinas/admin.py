from django.contrib import admin

from disciplinas.models import Disciplina

# Register your models here.

class ListandoDisciplinas(admin.ModelAdmin):
    
    list_display = ('nome', 'curso', 'id')

    def get_nome(self, obj):
        return obj.nome
    def get_curso(self, obj):
        return obj.curso
    
    get_nome.short_description = 'Nome'  #Renames column head
    get_curso.short_description = 'Pertence ao curso:'  #Renames column head

admin.site.register(Disciplina, ListandoDisciplinas)