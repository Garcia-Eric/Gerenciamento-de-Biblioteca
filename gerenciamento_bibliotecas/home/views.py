from django.shortcuts import render
from django.conf import settings
from .forms import CategoriaForm, GeneroForm, LocalizacaoForm


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


def create_book(request):
    context = {}
    context['form_categoria'] = CategoriaForm()
    context['form_genero'] = GeneroForm()
    context['form_localizacao'] = LocalizacaoForm()
    return render(request, 'home/cadastro_livro.html', context)
