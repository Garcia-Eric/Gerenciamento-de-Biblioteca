from django import forms
from .models import Genero


class CategoriaForm(forms.Form):
    CATEGORIA_CHOICES = [
        ("INFANTIL", "Infantil"),
        ("JUVENIL", "Juvenil"),
        ("ADULTO", "Adulto")
    ]
    categoria_field = forms.ChoiceField(
        label='Categoria', choices=CATEGORIA_CHOICES)


class GeneroForm(forms.Form):
    GENERO_CHOICES = Genero.get_generos()
    genero_field = forms.ChoiceField(
            label='Gênero', choices=GENERO_CHOICES)


class LocalizacaoForm(forms.Form):
    LOCALIZACAO_CHOICES = [
        ('000', 'Generalidades'),
        ('100', 'Filosofia e Psicologia'),
        ('200', 'Religião'),
        ('300', 'Ciências sociais'),
        ('400', 'Língua e Linguagem'),
        ('500', 'Ciências Puras'),
        ('600', 'Tecnologia e ciências aplicadas'),
        ('700', 'Artes/Esportes e Recreação'),
        ('800', 'Literatura'),
        ('900', 'Geografia/História/Biografia'),
    ]
    localizacao_field = forms.ChoiceField(
        label='Local', choices=LOCALIZACAO_CHOICES)
