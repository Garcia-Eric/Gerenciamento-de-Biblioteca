from django import forms
from .models import Genero, Emprestimo, Livro
from django.conf import settings

class FormLivro(forms.Form):
    CATEGORIA_CHOICES = Livro.get_categorias()
    GENERO_CHOICES = Genero.get_generos()    
    LOCALIZACAO_CHOICES = Livro.get_localizacao()
    
    titulo_livro = forms.CharField(label="Título do livro", max_length=100)    
    nome_autor = forms.CharField(label="Nome autor",max_length=75)
    editora = forms.CharField(label="Editora",max_length=50)
    genero = forms.ChoiceField(label="Gênero",choices=GENERO_CHOICES)
    localizacao = forms.ChoiceField(label="Localização",choices=LOCALIZACAO_CHOICES)
    categoria = forms.ChoiceField(label="Categoria",choices=CATEGORIA_CHOICES)
    sinopse = forms.CharField(label='Sinopse', max_length=512)
    src_imagem = forms.CharField(label='Source capa do livro', required=False)
    
    def save(self, tit, aut, edi, gen, loc, cat, sin, src):
        Livro.save_livro(tit, aut, edi, gen, loc, cat, sin, src)


# class FormEmprestimo(forms.Form):
#     from django.contrib.auth import get_user_model
#     lista_livros_disponiveis = Livro.get_livros_disponiveis()
#     LIVROS_DISPONIVEIS = [(livro.id, livro.titulo_livro) for livro in lista_livros_disponiveis]
    
#     User = get_user_model()
#     users = [(user.id, user.username) for user in User.objects.all()]
#     usuarios = forms.ChoiceField(label="Livros disponíveis para empréstimo",choices=users)
#     livro_emprestimo = forms.ChoiceField(label="Livros disponíveis para empréstimo",choices=LIVROS_DISPONIVEIS)
    