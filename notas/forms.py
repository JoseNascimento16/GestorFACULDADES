from django import forms
from .validation import *
from .models import Nota
from cursos.models import Curso
from disciplinas.models import Disciplina
from bootstrap_datepicker_plus.widgets import DatePickerInput

# from tempus_dominus.widgets import DatePicker


class NotaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.disciplina_super = kwargs.pop('disciplina_super', None)
        self.aluno_super = kwargs.pop('aluno_super', None)
        super().__init__(*args, **kwargs)

    # a disciplina foi configurada na views
    class Meta:

        model = Nota
        fields = ['aluno', 'disciplina', 'nota']
        labels = {
            # 'aluno':'Aluno',
            # 'disciplina':'Disciplina:',
            'nota':'Nota:',
        }
        widgets = {
            # 'aluno': forms.TextInput(attrs={'placeholder': 'Nome do Aluno...','class': 'fonte-italic','required':''}),
            'nota': forms.NumberInput(attrs={'placeholder': 'Nota do aluno...','min':'0','max':'10','class': 'fonte-italic'}),
        }

    def clean(self):
        aluno = self.aluno_super
        disciplina = self.disciplina_super
        nota_disciplina = self.cleaned_data.get('nota')
        lista_de_erros = {}

        nota_ja_existe(nota_disciplina, aluno, disciplina, 'nota', lista_de_erros)

        if lista_de_erros is not None:
            for erro in lista_de_erros:
                mensagem_erro = lista_de_erros[erro]
                self.add_error(erro, mensagem_erro)
        return self.cleaned_data