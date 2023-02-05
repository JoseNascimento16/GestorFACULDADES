from django.shortcuts import render, redirect, get_object_or_404
from alunos.models import Aluno
from professores.models import Professor
from .models import Disciplina
from notas.models import Nota
from .forms import DisciplinaForm

# Create your views here.

def disciplina(request, **kwargs):
    disciplina_obj = ''
    disciplina = Disciplina.objects.all()
    form = DisciplinaForm()

    form_com_erros = False
    if kwargs.get('form'):
        form_com_erros = True
        form = kwargs['form']

    form_populado = False
    if kwargs.get('populated_form'):
        form_populado = True
        form = kwargs['populated_form']
        disciplina_obj = get_object_or_404(Disciplina, pk=kwargs['disciplina_id'])

    contexto = {
        'chave_disciplinas': disciplina,
        'chave_form' : form,
        'erro_form_disciplina' : form_com_erros,
        'form_disciplina_populado' : form_populado,
        'disciplina_obj' : disciplina_obj
    }
    return render(request, 'cadastro-disciplina.html', contexto)

def cadastro_de_disciplina(request, **kwargs):
    if request.method == 'POST':
        form = DisciplinaForm(request.POST)
        if form.is_valid():
            # nome_curso = form.cleaned_data.get('nome')
            form.save()
        else:
            return disciplina(request, form=form)
    return redirect('disciplinas')

def update_disciplina(request, **kwargs):
    disciplina_obj = get_object_or_404(Disciplina, pk=kwargs['disciplina_id'])

    if request.method == 'POST':
        form = DisciplinaForm(request.POST, instance=disciplina_obj)
        if form.is_valid():
            form.save()
            return redirect('disciplinas')
        else:
            form.fields['curso'].initial = disciplina_obj.curso
            form.fields['curso'].disabled = True
            return disciplina(request, populated_form=form, disciplina_id=kwargs['disciplina_id'])

    form = DisciplinaForm(instance=disciplina_obj)
    form.fields['curso'].initial = disciplina_obj.curso
    form.fields['curso'].disabled = True
    return disciplina(request, populated_form=form, disciplina_id=kwargs['disciplina_id'])

def delete_disciplina(request, **kwargs):
    disciplina_obj = get_object_or_404(Disciplina, pk=kwargs['disciplina_id'])
    disciplina_obj.delete()
    
    return redirect('disciplinas')

def entra_disciplina(request, **kwargs):
    disciplina = get_object_or_404(Disciplina, id=kwargs['disciplina_id'])
    professor = disciplina.professor_set.first
    alunos = disciplina.aluno_set.all()
    notas = Nota.objects.filter(disciplina=disciplina.id)
    contexto = {
        'obj_disciplina': disciplina,
        'obj_professor' : professor,
        'alunos_da_disciplina' : alunos,
        'notas_da_disciplina' : notas
    }
    return render(request, 'disciplina.html', contexto)