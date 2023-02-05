from django.shortcuts import render, redirect, get_object_or_404
from alunos.models import Aluno
from notas.models import Nota
from .models import Curso
from professores.models import Professor
from .forms import CursoForm

# Create your views here.

def curso(request, **kwargs):
    curso_obj = ''
    cursos = Curso.objects.all()
    form = CursoForm()

    form_com_erros = False
    if kwargs.get('form'):
        form_com_erros = True
        form = kwargs['form']

    form_populado = False
    if kwargs.get('populated_form'):
        form_populado = True
        form = kwargs['populated_form']
        curso_obj = get_object_or_404(Curso, pk=kwargs['curso_id'])

    contexto = {
        'chave_cursos': cursos,
        'chave_form' : form,
        'erro_form_curso' : form_com_erros,
        'form_curso_populado' : form_populado,
        'curso_obj' : curso_obj
    }
    return render(request, 'cadastro-curso.html', contexto)

def cadastro_de_curso(request, **kwargs):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            # nome_curso = form.cleaned_data.get('nome')
            form.save()
        else:
            return curso(request, form=form)
    return redirect('cursos')

def update_curso(request, **kwargs):
    curso_obj = get_object_or_404(Curso, pk=kwargs['curso_id'])

    if request.method == 'POST':
        form = CursoForm(request.POST, instance=curso_obj)
        if form.is_valid():
            form.save()
            return redirect('cursos')
        else:
            return curso(request, populated_form=form, curso_id=kwargs['curso_id'])

    form = CursoForm(instance=curso_obj)
    return curso(request, populated_form=form, curso_id=kwargs['curso_id'])
    
def delete_curso(request, **kwargs):
    curso_obj = get_object_or_404(Curso, pk=kwargs['curso_id'])
    curso_obj.delete()

    return redirect('cursos')

def entra_curso(request, **kwargs):
    curso = get_object_or_404(Curso, id=kwargs['curso_id'])
    disciplinas = curso.disciplina_set.all()
    contexto = {
        'obj_curso': curso,
        'disciplinas_do_curso' : disciplinas,
    }
    return render(request, 'curso.html', contexto)

def indexar(request):
    cursos = Curso.objects.all()
    todos_professores = Professor.objects.all()
    todos_alunos = Aluno.objects.all()
    todas_notas = Nota.objects.all()
    contexto = {
        'chave_cursos' : cursos,
        'chave_professores' : todos_professores,
        'chave_alunos' : todos_alunos,
        'chave_notas' : todas_notas
    }
    return render(request, 'index.html', contexto)
