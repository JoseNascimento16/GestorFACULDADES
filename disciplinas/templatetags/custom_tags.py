from statistics import mean
from django import template
register = template.Library()

@register.simple_tag
def get_notas(obj_disciplina, aluno):
    nota_query = aluno.nota_set.filter(disciplina=obj_disciplina)
    for nota_obj in nota_query:
        return nota_obj

@register.simple_tag
def get_professores(curso, chave_professores):
    count = 0
    for professor in chave_professores:
        if professor.disciplina:
            if professor.disciplina.curso == curso:
                count+=1
    if count:
        return count
    else:
        return 0

@register.simple_tag
def get_alunos(curso, chave_alunos):
    count = 0
    for aluno in chave_alunos:
        if aluno.curso == curso:
            count+=1
    if count:
        return count
    else:
        return 0

@register.simple_tag
def get_media_por_curso(curso, chave_notas):
    lista = []
    for nota in chave_notas:
        if nota.aluno.curso == curso:
            lista.append(nota.nota)
    if lista:
        return round(mean(lista), 1)
    else:
        return '-----'

@register.simple_tag
def quant_alunos_disciplina(obj_disciplina):
    quant_alunos = obj_disciplina.aluno_set.all()
    return len(quant_alunos)

@register.simple_tag
def verifica_professor(disciplina):
    professor = disciplina.professor_set.first()
    if professor:
        return professor
    else:
        return '-----'

@register.simple_tag
def verifica_disciplina(professor):
    disciplina = professor.disciplina
    if disciplina:
        return disciplina
    else:
        return '-----'

@register.simple_tag
def verifica_curso(aluno):
    curso = aluno.curso
    if curso:
        return curso
    else:
        return '-----'