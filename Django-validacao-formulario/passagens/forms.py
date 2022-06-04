from django import forms
from django.forms import Textarea
from tempus_dominus.widgets import DatePicker
from datetime import datetime
from passagens.classe_viagem import tipos_de_classe
from passagens.validation import *
from passagens.models import Passagem, ClasseViagem, Pessoa


class PassagemForms(forms.ModelForm):
    data_pesquisa = forms.DateField(label='Data da pesquisa', disabled=True, initial=datetime.today())

    class Meta:
        model = Passagem
        fields = '__all__'
        labels = {'data_ida': 'Data de ida', 'data_volta': 'Data de volta', 'informacoes': 'Informações', 'classe_viagem': 'Classe do vôo'}
        widgets = {
            'data_ida': DatePicker(),
            'data_volta': DatePicker(),
        }
    # origem = forms.CharField(label='Origem', max_length=100)
    # destino = forms.CharField(label='Destino', max_length=100)
    # data_ida = forms.DateField(label='Ida', widget=DatePicker())
    # data_volta = forms.DateField(label='Volta', widget=DatePicker())
    # classe_viagem = forms.ChoiceField(label='Classe do vôo', choices=tipos_de_classe)
    # informacoes = forms.CharField(label='Informações extra', max_length=200, widget=Textarea(), required=False)
    # email = forms.EmailField(label='e-mail', max_length=150)

    def clean(self):
        origem = self.cleaned_data.get('origem')
        destino = self.cleaned_data.get('destino')
        data_ida = self.cleaned_data.get('data_ida')
        data_volta = self.cleaned_data.get('data_volta')
        data_pesquisa = self.cleaned_data.get('data_pesquisa')

        lista_erros = {}

        caractere_numerico(origem, 'origem', lista_erros)

        caractere_numerico(destino, 'destino', lista_erros)

        origem_destino_iguais(origem, destino, lista_erros)

        valida_data(data_ida, data_volta, data_pesquisa, lista_erros)

        if lista_erros is not None:
            for erro in lista_erros:
                mensagem_erro = lista_erros[erro]
                self.add_error(erro, mensagem_erro)
        return self.cleaned_data


class PessoaForms(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = ['email']
