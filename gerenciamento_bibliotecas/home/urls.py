from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    
    # Cadastros
    path('cadastrar_livros/', views.create_book_form, name='cadastro_livros'),
    path('cadastrar_usuarios/', views.create_user, name='cadastro_usuario'),
    path('cadastrar_emprestimos/', views.create_book_lending, name='cadastro_emprestimo'),
    
    
    # Consultas
    path('consultar_livros/', views.get_books, name='consultar_livros'),
    path('informacoes_livro/<int:id>', views.get_book_information, name='informacoes_livro'),    
    path('consultar_usuarios/', views.get_users, name='consultar_usuarios'),
    path('consultar_emprestimos/', views.get_lendings, name='consultar_emprestimos'),
]
