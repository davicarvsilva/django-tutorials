from django import forms

from .models import Pessoa, Musica


class PessoaForm(forms.ModelForm):
    class Meta:
        model =  Pessoa
        fields = ['nome']

class MusicaForm(forms.ModelForm):
    class Meta:
        model =  Musica
        fields = ['nome']