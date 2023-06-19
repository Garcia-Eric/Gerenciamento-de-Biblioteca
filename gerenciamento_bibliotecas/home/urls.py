from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('cadastrar_livros/', views.create_book_form, name='cadastro_livros')
]
