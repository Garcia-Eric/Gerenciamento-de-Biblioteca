from django import forms
from .models import Genero, Emprestimo, Livro, Usuario
from django.conf import settings
import datetime

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


class FormUsuario(forms.Form):
    cpf = forms.CharField(max_length=11)
    nome_completo = forms.CharField(max_length=70)
    email = forms.EmailField(max_length=255)
    telefone = forms.CharField(max_length=12)
    
    def save(self, cpf, nome, email, telefone):
        Usuario.save_usuario(cpf, nome, email, telefone)    


class FormEmprestimo(forms.Form):

    lista_livros_disponiveis = Livro.get_livros_disponiveis()
    LIVROS_DISPONIVEIS = [(livro.id, livro.titulo_livro) for livro in lista_livros_disponiveis]
    livro_emprestimo = forms.ChoiceField(label="Livros disponíveis para empréstimo",choices=LIVROS_DISPONIVEIS)
    
    lista_usuarios_disponiveis = Usuario.get_usuarios_disponiveis()
    users = [(user.cpf, user.nome_completo) for user in lista_usuarios_disponiveis]
    usuarios = forms.ChoiceField(label="Livros disponíveis para empréstimo",choices=users)
    
    hoje = datetime.date.today()
    DIAS_MES = 31
    daqui_2_meses = hoje + datetime.timedelta(days=DIAS_MES * 2)
    data_devolucao = forms.DateField(label="Data devolução", initial=daqui_2_meses)
    
    def save(self, fk_livro, fk_user, data_devolucao):
        Emprestimo.create_emprestimo(fk_livro, fk_user, data_devolucao)