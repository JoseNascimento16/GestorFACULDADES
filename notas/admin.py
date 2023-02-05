from django.contrib import admin

from notas.models import Nota

# Register your models here.

class ListandoNotas(admin.ModelAdmin):
    
    list_display = ('aluno', 'disciplina', 'nota', 'id')

    def get_aluno(self, obj):
        return obj.aluno
    def get_disciplina(self, obj):
        return obj.disciplina
    def get_nota(self, obj):
        return obj.nota
    
    get_aluno.short_description = 'Aluno'  #Renames column head
    get_disciplina.short_description = 'Disciplina'  #Renames column head
    get_nota.short_description = 'Nota'  #Renames column head

admin.site.register(Nota, ListandoNotas)