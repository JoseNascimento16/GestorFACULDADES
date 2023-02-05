from django import forms
from .validation import *
from .models import Curso

# from tempus_dominus.widgets import DatePicker


class CursoForm(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     self.curso_super = kwargs.pop('curso_super', None)
    #     super().__init__(*args, **kwargs)
        
    class Meta:

        model = Curso
        fields = ['nome']
        labels = {
            'nome':'Nome do curso:',
        }
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Insira aqui...','class': 'fonte-italic','required':''}),
        }

    def clean(self):
        # escola = self.escola_super
        nome_curso = self.cleaned_data.get('nome')
        lista_de_erros = {}

        curso_ja_existe(nome_curso, 'nome', lista_de_erros)

        if lista_de_erros is not None:
            for erro in lista_de_erros:
                mensagem_erro = lista_de_erros[erro]
                self.add_error(erro, mensagem_erro)
        return self.cleaned_data