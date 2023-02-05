from django.shortcuts import render, redirect, get_object_or_404
from django import forms
from .models import Aluno
from .forms import AlunoForm
from disciplinas.models import Disciplina
from notas.forms import NotaForm
from notas.models import Nota

# Create your views here.

def aluno(request, **kwargs):
    aluno_obj = ''
    alunos = Aluno.objects.all()
    form = AlunoForm()

    form_com_erros = False
    if kwargs.get('form'):
        form_com_erros = True
        form = kwargs['form']

    form_populado = False
    if kwargs.get('populated_form'):
        form_populado = True
        form = kwargs['populated_form']
        aluno_obj = get_object_or_404(Aluno, pk=kwargs['aluno_id'])

    contexto = {
        'chave_alunos': alunos,
        'chave_form' : form,
        'erro_form_aluno' : form_com_erros,
        'form_aluno_populado' : form_populado,
        'aluno_obj' : aluno_obj
    }
    return render(request, 'cadastro-aluno.html', contexto)

def cadastro_de_aluno(request, **kwargs):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            return aluno(request, form=form)
    return redirect('alunos')

def update_aluno(request, **kwargs):
    aluno_obj = get_object_or_404(Aluno, pk=kwargs['aluno_id'])

    if request.method == 'POST':
        form = AlunoForm(request.POST, instance=aluno_obj, updating=True)
        if form.is_valid():
            form.save()
            return redirect('alunos')
        else:
            if aluno_obj.curso:
                form.fields['curso'].initial = aluno_obj.curso
                form.fields['curso'].disabled = True
            return aluno(request, populated_form=form, aluno_id=kwargs['aluno_id'])

    form = AlunoForm(instance=aluno_obj)
    if aluno_obj.curso:
        form.fields['curso'].initial = aluno_obj.curso
        form.fields['curso'].disabled = True
    return aluno(request, populated_form=form, aluno_id=kwargs['aluno_id'])

def delete_aluno(request, **kwargs):
    aluno_obj = get_object_or_404(Aluno, pk=kwargs['aluno_id'])
    notas = Nota.objects.filter(aluno=aluno_obj)
    for nota in notas:
        nota.delete()
    aluno_obj.delete()
    
    return redirect('alunos')

def entra_aluno(request, **kwargs):
    nota_obj = ''
    aluno = get_object_or_404(Aluno, id=kwargs['aluno_id'])
    # disciplinas = aluno.cursando_disciplina.all()
    notas_do_aluno = Nota.objects.filter(aluno=aluno)

    NotaForm.base_fields['disciplina'] = forms.ModelChoiceField( ###
	queryset=Disciplina.objects.filter(curso=aluno.curso), #
	empty_label="------------",
        label='Disciplina:',
        required=True,
        widget=forms.Select)

    NotaForm.base_fields['aluno'] = forms.ModelChoiceField( ###
	queryset=Aluno.objects.filter(nome=aluno.nome), #
	empty_label="------------",
        label='Aluno:',
        required=True,
        widget=forms.Select)

    form = NotaForm()
    form.fields['aluno'].initial = aluno
    form.fields['aluno'].disabled = True

    form_com_erros = False
    if kwargs.get('form'):
        form_com_erros = True
        form = kwargs['form']
        form.fields['aluno'].initial = aluno
        form.fields['aluno'].disabled = True

    form_populado = False
    if kwargs.get('populated_form'):
        form_populado = True
        form = kwargs['populated_form']
        nota_obj = get_object_or_404(Nota, pk=kwargs['nota_id'])

    contexto = {
        'obj_aluno' : aluno,
        # 'lista_de_disciplinas' : disciplinas,
        'lista_de_notas' : notas_do_aluno,
        'chave_form' : form,
        'erro_form_nota' : form_com_erros,
        'form_nota_populado' : form_populado,
        'nota_obj' : nota_obj
    }
    return render(request, 'aluno.html', contexto)