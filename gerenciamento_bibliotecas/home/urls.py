from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('cadastrar_livros/', views.create_book_form, name='cadastro_livros'),
    path('consultar_livros/', views.get_books, name='consultar_livros'),
    path('informacoes_livro/<int:id>', views.get_book_information, name='informacoes_livro')
]
