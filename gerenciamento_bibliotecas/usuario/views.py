from django.shortcuts import render

def login(request):
    return render(request, 'usuario/login.html')