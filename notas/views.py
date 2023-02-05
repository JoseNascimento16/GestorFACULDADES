from django.shortcuts import render, redirect, get_object_or_404
from .forms import NotaForm
from alunos.views import entra_aluno
from alunos.models import Aluno
from .models import Nota

# Create your views here.

def cadastro_de_nota(request, **kwargs):
    if request.method == 'POST':
        aluno_id = request.POST.get('aluno')
        form = NotaForm(request.POST, disciplina_super=request.POST.get('disciplina'), aluno_super=request.POST.get('aluno'))
        if form.is_valid():
            disciplina = form.cleaned_data.get('disciplina')
            aluno = get_object_or_404(Aluno, pk=aluno_id)
            aluno.cursando_disciplina.add(disciplina)
            aluno.save()
            form.save()
        else:
            return entra_aluno(request, aluno_id=aluno_id, form=form)
    return redirect('entrando_aluno', aluno_id=request.POST.get('aluno'))

def update_nota(request, **kwargs):
    nota_obj = get_object_or_404(Nota, pk=kwargs['nota_id'])

    if request.method == 'POST':
        form = NotaForm(request.POST, instance=nota_obj)
        if form.is_valid():
            form.save()
            return redirect('entrando_aluno', aluno_id=nota_obj.aluno.id)
        else:
            form.fields['aluno'].initial = nota_obj.aluno
            form.fields['aluno'].disabled = True
            return entra_aluno(request, populated_form=form, nota_id=kwargs['nota_id'], aluno_id=nota_obj.aluno.id)

    form = NotaForm(instance=nota_obj)
    form.fields['aluno'].initial = nota_obj.aluno
    form.fields['aluno'].disabled = True
    return entra_aluno(request, populated_form=form, nota_id=kwargs['nota_id'], aluno_id=nota_obj.aluno.id)

def delete_nota(request, **kwargs):
    nota_obj = get_object_or_404(Nota, pk=kwargs['nota_id'])
    aluno = get_object_or_404(Aluno, pk=nota_obj.aluno.id)
    nota_obj.delete()
    return redirect('entrando_aluno', aluno_id=aluno.id)