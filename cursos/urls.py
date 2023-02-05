from django.urls import path
from . import views

urlpatterns = [
    path('',views.indexar, name='index'),
    path('cursos',views.curso, name='cursos'),
    path('cadastro/curso',views.cadastro_de_curso, name='cadastra_curso'),
    path('chama/update/curso/<int:curso_id>',views.update_curso, name='chama_update_curso'),
    path('update/curso/<int:curso_id>',views.update_curso, name='update_curso'),
    path('exclui/curso/<int:curso_id>',views.delete_curso, name='deletando_curso'),
    path('curso/<int:curso_id>',views.entra_curso, name='entrando_curso'),
]