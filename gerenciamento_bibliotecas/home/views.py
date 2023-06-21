from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.conf import settings
from . import forms, models


def home(request):
    context = {
        'usuarios': [
            {
                'nome': 'Gianluca',
                'livro': 'Chapeuzinho Vermelho',
                'dias_vencidos': 13,
            },
            {
                'nome': 'Diogo',
                'livro': 'O Poder do Agora',
                'dias_vencidos': 19,
            },
            {
                'nome': 'Eric',
                'livro': 'Revolução dos Bixos',
                'dias_vencidos': 22,
            },
        ],
        'livros': [
            {
                'nome': 'Guia do Mochileiro das Galáxias',
                'imagem': f'{settings.STATIC_URL}images/livros/guia_do_mochileiro_das_galaxias.jpg',
            }
        ],
    }

    return render(request, 'home/home.html', context)


def create_book_form(request):
    if request.method == "POST":  
        formulario = forms.FormLivro(request.POST)     
        if formulario.is_valid():
            info_livro = {
                'titulo': request.POST.get('titulo_livro'),
                'autor': request.POST.get('nome_autor'),
                'editora': request.POST.get('editora'),
                'gen': request.POST.get('genero'),
                'loc': request.POST.get('localizacao'),
                'cat': request.POST.get('categoria'),
                'sin': request.POST.get('sinopse'),
                'src': request.POST.get('src_imagem'),
            }
            formulario.save(info_livro['titulo'],
                            info_livro['autor'],
                            info_livro['editora'],
                            info_livro['gen'],
                            info_livro['loc'],
                            info_livro['cat'],
                            info_livro['sin'],
                            info_livro['src'],
                            )
            return HttpResponseRedirect(request.path_info)
    else:
        formulario = forms.FormLivro()        
    return render(request, 'home/livros/cadastro_livro.html', {'form':forms.FormLivro()})


def get_books(request):
    livros_emprestados = models.Livro.get_livros_emprestados()
    livros_disponiveis = models.Livro.get_livros_disponiveis()
    context = {'emprestados':livros_emprestados,
               'disponiveis':livros_disponiveis}
    return render(request, 'home/livros/consultar_livros.html', context)
    

def get_book_information(request, id):
    livro = models.Livro.objects.get(id=id)
    context = {'livro':livro,
               'generos':livro.get_generos_livro(),
               'localizacao': {
                   'cod':livro.get_localizacao_livro()[0][0],
                   'significado':livro.get_localizacao_livro()[0][1]
                    }
                }
    return render(request, 'home/livros/info_livro.html', context)




def create_book_lending(request):
    if request.method == "POST":  
        formulario = forms.FormEmprestimo(request.POST)     
        if formulario.is_valid():
            return HttpResponseRedirect(request.path_info)
    else:
        formulario = forms.FormEmprestimo()        
    return render(request, 'home/emprestimos/cadastro_emprestimo.html', {'form':forms.FormEmprestimo()})