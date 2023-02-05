from django.urls import path
from . import views

urlpatterns = [
    path('professores',views.professor, name='professores'),
    path('cadastro/professor',views.cadastro_de_professor, name='cadastra_professor'),
    path('chama/update/professor/<int:professor_id>',views.update_professor, name='chama_update_professor'),
    path('update/professor/<int:professor_id>',views.update_professor, name='update_professor'),
    path('exclui/professor/<int:professor_id>',views.delete_professor, name='deletando_professor'),
]