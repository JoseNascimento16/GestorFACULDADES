from django.contrib import admin

from professores.models import Professor

# Register your models here.

class ListandoProfessor(admin.ModelAdmin):
    
    list_display = ('nome', 'disciplina', 'data_nascimento', 'salario', 'curso', 'id')

    def get_nome(self, obj):
        return obj.nome
    def get_disciplina(self, obj):
        return obj.disciplina
    def get_nascimento(self, obj):
        return obj.data_nascimento
    def get_salario(self, obj):
        return obj.salario
    
    get_nome.short_description = 'Nome'  #Renames column head
    get_disciplina.short_description = 'Disciplina'  #Renames column head
    get_nascimento.short_description = 'Data de nascimento'  #Renames column head
    get_salario.short_description = 'Salário'  #Renames column head

admin.site.register(Professor, ListandoProfessor)