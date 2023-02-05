from django.contrib import admin
from alunos.models import Aluno

# Register your models here.

class ListandoAlunos(admin.ModelAdmin):
    
    list_display = ('nome', 'matricula', 'data_nascimento', 'curso', 'id')

    def get_nome(self, obj):
        return obj.nome
    def get_matricula(self, obj):
        return obj.matricula
    def get_nascimento(self, obj):
        return obj.nascimento
    
    get_nome.short_description = 'Nome'  #Renames column head
    get_nome.short_description = 'Matrícula'  #Renames column head
    get_nome.short_description = 'Data de nascimento'  #Renames column head
    # get_username.admin_order_field  = 'username'  #Allows column order sorting

admin.site.register(Aluno, ListandoAlunos)