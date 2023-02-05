from .models import Aluno

def aluno_ja_existe(valor, campo, lista_de_erros):
    alunos = Aluno.objects.filter(nome=valor)
    if alunos.exists():
        lista_de_erros[campo] = 'Este aluno já é cadastrado na instituição...'