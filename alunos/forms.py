from django import forms
from .validation import *
from .models import Aluno
from cursos.models import Curso
from bootstrap_datepicker_plus.widgets import DatePickerInput

# from tempus_dominus.widgets import DatePicker


class AlunoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.updating = kwargs.pop('updating', None)
        super().__init__(*args, **kwargs)

    curso = forms.ModelChoiceField(
        queryset=Curso.objects.order_by('nome').all(),
        empty_label="------------",
        label='Curso:',
        widget=forms.Select)
        
    class Meta:

        model = Aluno
        fields = ['nome', 'data_nascimento', 'matricula', 'curso']
        labels = {
            'nome':'Nome do aluno:',
            'data_nascimento':'Data de nascimento:',
            'matricula':'Matrícula:',
            'curso':'Curso:',
        }
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Insira aqui...','class': 'fonte-italic','required':''}),
            'data_nascimento': DatePickerInput(options={'format':'DD-MM-YYYY'}, attrs={'placeholder': 'dd/mm/aaaa','class': 'fonte-italic'}),
            'matricula': forms.NumberInput(attrs={'placeholder': 'nº de matrícula...','min':'1','max':'100000','class': 'fonte-italic'}),
        }

    def clean(self):
        nome_aluno = self.cleaned_data.get('nome')
        lista_de_erros = {}

        if not self.updating:
            aluno_ja_existe(nome_aluno, 'nome', lista_de_erros)

        if lista_de_erros is not None:
            for erro in lista_de_erros:
                mensagem_erro = lista_de_erros[erro]
                self.add_error(erro, mensagem_erro)
        return self.cleaned_data