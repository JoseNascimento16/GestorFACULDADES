from .models import Nota

def nota_ja_existe(notas, aluno, disciplina, campo, lista_de_erros):
    notas = Nota.objects.filter(disciplina=disciplina).filter(aluno=aluno)
    if notas.exists():
        lista_de_erros[campo] = 'Já existe nota cadastrada para esta disciplina...'
    