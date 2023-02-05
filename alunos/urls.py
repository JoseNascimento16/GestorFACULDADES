from django.urls import path
from . import views

urlpatterns = [
    path('alunos',views.aluno, name='alunos'),
    path('cadastro/aluno',views.cadastro_de_aluno, name='cadastra_aluno'),
    path('chama/update/aluno/<int:aluno_id>',views.update_aluno, name='chama_update_aluno'),
    path('update/aluno/<int:aluno_id>',views.update_aluno, name='update_aluno'),
    path('exlcui/aluno/<int:aluno_id>',views.delete_aluno, name='deletando_aluno'),
    path('aluno/<int:aluno_id>',views.entra_aluno, name='entrando_aluno'),
]