from .models import Curso

def curso_ja_existe(valor, campo, lista_de_erros):
    cursos = Curso.objects.filter(nome=valor)
    if cursos.exists():
        lista_de_erros[campo] = 'Já existe um curso com este nome, escolha outro...'