from django.shortcuts import render

def home(request):
    context = {
        'usuarios': [
            {
                'nome': 'Gianluca',
                'livro': 'O Poder do Agora',
                'dias_vencidos': 19,
            }
        ]
    }

    return render(request, 'home/home.html', context)