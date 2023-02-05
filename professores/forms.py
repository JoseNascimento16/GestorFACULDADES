from django import forms
from .validation import *
from .models import Disciplina
from cursos.models import Curso
from bootstrap_datepicker_plus.widgets import DatePickerInput

# from tempus_dominus.widgets import DatePicker


class ProfessorForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.updating = kwargs.pop('updating', None)
        super().__init__(*args, **kwargs)

    disciplina = forms.ModelChoiceField(
        queryset=Disciplina.objects.order_by('nome').filter(professor=None),
        empty_label="------------",
        label='Disciplina: (Disponíveis)',
        widget=forms.Select)
        
    class Meta:

        model = Professor
        fields = ['nome', 'data_nascimento', 'salario', 'disciplina']
        labels = {
            'nome':'Nome do professor:',
            'data_nascimento':'Data de nascimento:',
            'salario':'Salário:',
        }
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Insira aqui...','class': 'fonte-italic','required':''}),
            'data_nascimento': DatePickerInput(options={'format':'DD-MM-YYYY'}, attrs={'placeholder': 'dd/mm/aaaa','class': 'fonte-italic'}),
            'salario': forms.NumberInput(attrs={'placeholder': 'Salário do professor...','min':'1','max':'100000','class': 'fonte-italic'}),
        }

    def clean(self):
        
        nome_professor = self.cleaned_data.get('nome')
        lista_de_erros = {}

        if not self.updating:
            professor_ja_existe(nome_professor, 'nome', lista_de_erros)

        if lista_de_erros is not None:
            for erro in lista_de_erros:
                mensagem_erro = lista_de_erros[erro]
                self.add_error(erro, mensagem_erro)
        return self.cleaned_data