from django.db import models
from alunos.models import Aluno
from disciplinas.models import Disciplina

# Create your models here.

class Nota(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.DO_NOTHING)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    nota = models.FloatField()

    def __str__(self):
        return 'Nota de ' + self.aluno.nome