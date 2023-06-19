from . import views
from django.urls import path

urlpatterns= [
    path('', views.home),
    path('/cadastrar_livros/', views.create_book, name='cadastro_livros')
]