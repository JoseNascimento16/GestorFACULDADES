from django.shortcuts import render, redirect, get_object_or_404
from django import forms
from .models import Professor
from .forms import ProfessorForm
from disciplinas.models import Disciplina
from django.db.models import Q

# Create your views here.

def professor(request, **kwargs):
    professor_obj = ''
    professores = Professor.objects.all()
    form = ProfessorForm()

    form_com_erros = False
    if kwargs.get('form'):
        form_com_erros = True
        form = kwargs['form']

    form_populado = False
    if kwargs.get('populated_form'):
        form_populado = True
        form = kwargs['populated_form']
        professor_obj = get_object_or_404(Professor, pk=kwargs['professor_id'])
        
    contexto = {
        'chave_professores': professores,
        'chave_form' : form,
        'erro_form_professor' : form_com_erros,
        'form_professor_populado' : form_populado,
        'professor_obj' : professor_obj
    }
    return render(request, 'cadastro-professor.html', contexto)

def cadastro_de_professor(request, **kwargs):
    if request.method == 'POST':
        form = ProfessorForm(request.POST)
        if form.is_valid():
            disciplina_obj = get_object_or_404(Disciplina, nome=form.cleaned_data.get('disciplina'))
            instancia = form.save(commit=False)
            instancia.curso = disciplina_obj.curso
            instancia.save()
        else:
            return professor(request, form=form)
    return redirect('professores')

def update_professor(request, **kwargs):
    professor_obj = get_object_or_404(Professor, pk=kwargs['professor_id'])

    if request.method == 'POST':
        form = ProfessorForm(request.POST, instance=professor_obj, updating=True)
        if form.is_valid():
            disciplina_obj = get_object_or_404(Disciplina, nome=form.cleaned_data.get('disciplina'))
            instance = form.save(commit=False)
            instance.curso = disciplina_obj.curso
            instance.save()
            return redirect('professores')
        else:
            return professor(request, populated_form=form, professor_id=kwargs['professor_id'])

    # DEFINE QUAL QUERYSET USAR NO FIELD 'disciplina'
    define_disciplina_field(professor_obj)
    ################################################

    form = ProfessorForm(instance=professor_obj)
    form.fields['disciplina'].initial = professor_obj.disciplina
    # form.fields['disciplina'].disabled = True
    return professor(request, populated_form=form, professor_id=kwargs['professor_id'])

def delete_professor(request, **kwargs):
    professor_obj = get_object_or_404(Professor, pk=kwargs['professor_id'])
    professor_obj.delete()
    
    return redirect('professores')

#################################################

def define_disciplina_field(professor_obj):
    if professor_obj.disciplina:
        ProfessorForm.base_fields['disciplina'] = forms.ModelChoiceField( 
        queryset=Disciplina.objects.filter(Q(nome=professor_obj.disciplina.nome) | (Q(professor=None) & Q(curso=professor_obj.disciplina.curso))), 
        empty_label="------------",
            label='Disciplina: (Disponíveis)',
            required=True,
            widget=forms.Select)
    elif professor_obj.curso:
        ProfessorForm.base_fields['disciplina'] = forms.ModelChoiceField( 
        queryset=Disciplina.objects.filter(Q(curso=professor_obj.curso) & Q(professor=None)), 
        empty_label="------------",
            label='Disciplina: (Disponíveis)',
            required=True,
            widget=forms.Select)
    else:
        ProfessorForm.base_fields['disciplina'] = forms.ModelChoiceField( 
        queryset=Disciplina.objects.filter(professor=None), 
        empty_label="------------",
            label='Disciplina: (Disponíveis)',
            required=True,
            widget=forms.Select)