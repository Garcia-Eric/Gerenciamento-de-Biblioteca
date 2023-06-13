from django.shortcuts import render

def home(request):
    context = {
        'usuarios': [
            {
                'nome': 'Gianluca',
                'livro': 'Chapelzinho Vermelho',
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
        ]
    }

    return render(request, 'home/home.html', context)