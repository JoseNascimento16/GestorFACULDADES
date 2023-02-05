from .models import Professor

def professor_ja_existe(valor, campo, lista_de_erros):
    professores = Professor.objects.filter(nome=valor)
    if professores.exists():
        lista_de_erros[campo] = 'Este professor já tem cadastro na instituição...'