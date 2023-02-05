from django.db import models
from disciplinas.models import Disciplina
from cursos.models import Curso

# Create your models here.

class Professor(models.Model):
    disciplina = models.ForeignKey(Disciplina, on_delete=models.SET_NULL, null=True, blank=True)
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    salario = models.IntegerField()
    curso = models.ForeignKey(Curso, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nome