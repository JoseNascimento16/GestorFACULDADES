from django.urls import path
from . import views

urlpatterns = [
    path('disciplinas',views.disciplina, name='disciplinas'),
    path('cadastro/disciplina',views.cadastro_de_disciplina, name='cadastra_disciplina'),
    path('chama/update/disciplina/<int:disciplina_id>',views.update_disciplina, name='chama_update_disciplina'),
    path('update/disciplina/<int:disciplina_id>',views.update_disciplina, name='update_disciplina'),
    path('exclui/disciplina/<int:disciplina_id>',views.delete_disciplina, name='deletando_disciplina'),
    path('disciplina/<int:disciplina_id>',views.entra_disciplina, name='entrando_disciplina'),
]