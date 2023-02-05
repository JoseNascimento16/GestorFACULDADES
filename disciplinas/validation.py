from .models import Disciplina

def disciplina_ja_existe(valor, campo, lista_de_erros):
    disciplinas = Disciplina.objects.filter(nome=valor)
    if disciplinas.exists():
        lista_de_erros[campo] = 'Já existe uma disciplina com este nome, defina outra...'