from django import forms
from .models import Genero, Livro

class FormLivro(forms.Form):
    CATEGORIA_CHOICES = [
        ("INFANTIL", "Infantil"),
        ("JUVENIL", "Juvenil"),
        ("ADULTO", "Adulto")
    ]
    GENERO_CHOICES = Genero.get_generos()    
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
    
    titulo_livro = forms.CharField(label="Título do livro", max_length=100)    
    nome_autor = forms.CharField(label="Nome autor",max_length=75)
    editora = forms.CharField(label="Editora",max_length=50)
    genero = forms.ChoiceField(label="Gênero",choices=GENERO_CHOICES) # type: ignore
    localizacao = forms.ChoiceField(label="Localização",choices=LOCALIZACAO_CHOICES)
    categoria = forms.ChoiceField(label="Categoria",choices=CATEGORIA_CHOICES)
    sinopse = forms.CharField(label='Sinopse', max_length=512)
    src_imagem = forms.CharField(label='Source capa do livro', required=False)
    
    def save(self, tit, aut, edi, gen, loc, cat, sin, src):
        Livro.save_livro(tit, aut, edi, gen, loc, cat, sin, src)