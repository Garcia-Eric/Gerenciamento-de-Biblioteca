from django.db import models

# Create your models here.
class Genero(models.Model):
    tipo_genero = models.CharField(max_length=50)

    @classmethod
    def get_generos(cls) -> list[int, str]:
        return list(Genero.objects.all().values_list('id', 'tipo_genero'))

    def __str__(self) -> str:
        return f"{self.tipo_genero}"

    class Meta():
        db_table = 'genero'
        ordering = ['tipo_genero']


class Livro(models.Model):
    titulo_livro = models.CharField(max_length=100)
    nome_autor = models.CharField(max_length=75)
    editora = models.CharField(max_length=50)
    genero = models.ManyToManyField(Genero)
    localizacao = models.CharField(max_length=3)
    categoria = models.CharField(max_length=10)
    sinopse = models.TextField(max_length=512)
    src_imagem = models.TextField()
      
    @classmethod
    def save_livro(cls, tit, aut, edi, gen, loc, cat, sin, src):
        genero = Genero.objects.filter(id=gen)
        
        livro = Livro.objects.create(titulo_livro=tit,
                        nome_autor=aut,
                        editora=edi,                        
                        localizacao=loc,
                        categoria=cat,
                        sinopse=sin,
                        src_imagem=src
                    )
        livro.genero.set(genero)
        livro.save()
      
    class Meta():
        db_table = 'livro'
        ordering = ['titulo_livro']