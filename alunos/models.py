from django.db import models
from cursos.models import Curso
from disciplinas.models import Disciplina

# Create your models here.

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    matricula = models.IntegerField()
    data_nascimento = models.DateField()
    cursando_disciplina = models.ManyToManyField(Disciplina, blank=True)
    curso = models.ForeignKey(Curso, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return self.nome