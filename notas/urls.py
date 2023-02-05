from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/nota',views.cadastro_de_nota, name='cadastra_nota'),
    path('chama/update/nota/<int:nota_id>',views.update_nota, name='chama_update_nota'),
    path('update/nota/<int:nota_id>',views.update_nota, name='update_nota'),
    path('deleta/nota/<int:nota_id>', views.delete_nota, name='deletando_nota')
]