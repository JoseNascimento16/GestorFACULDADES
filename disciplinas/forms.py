from django import forms
from .validation import *
from .models import Disciplina
from cursos.models import Curso

# from tempus_dominus.widgets import DatePicker


class DisciplinaForm(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     self.curso_super = kwargs.pop('curso_super', None)
    #     super().__init__(*args, **kwargs)

    curso = forms.ModelChoiceField(
        queryset=Curso.objects.order_by('nome').all(),
        empty_label="------------",
        label='Curso:',
        widget=forms.Select)
        
    class Meta:

        model = Disciplina
        fields = ['curso', 'nome']
        labels = {
            'nome':'Nome da disciplina:',
        }
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Insira aqui...','class': 'fonte-italic','required':''}),
        }

    def clean(self):
        # escola = self.escola_super
        nome_disciplina = self.cleaned_data.get('nome')
        lista_de_erros = {}

        disciplina_ja_existe(nome_disciplina, 'nome', lista_de_erros)

        if lista_de_erros is not None:
            for erro in lista_de_erros:
                mensagem_erro = lista_de_erros[erro]
                self.add_error(erro, mensagem_erro)
        return self.cleaned_data