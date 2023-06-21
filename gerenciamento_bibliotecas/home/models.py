from django.conf import settings
from django.db import models
import datetime

# Create your models here.

class Usuario(models.Model):
    cpf = models.CharField(max_length=11, primary_key=True, unique=True)
    nome_completo = models.CharField(max_length=70)
    email = models.EmailField(max_length=255)
    telefone = models.CharField(max_length=12)
    dependentes = models.ForeignKey("self", on_delete=models.DO_NOTHING, null=True, blank=True)    
    
    def get_cpf(self):
        return f"{self.cpf[0:3]}.{self.cpf[3:6]}.{self.cpf[6:9]}-{self.cpf[9:12]}"
    def __str__(self) -> str:
        return f"{self.get_cpf()} - {self.nome_completo}"
    
    class Meta():
        db_table = 'usuarios'

class Genero(models.Model):
    tipo_genero = models.CharField(max_length=50)

    @classmethod
    def get_generos(cls):
        return list(Genero.objects.all().values_list('id', 'tipo_genero'))

    def __str__(self) -> str:
        return f"{self.tipo_genero}"

    class Meta():
        db_table = 'genero'
        ordering = ['tipo_genero']


class Livro(models.Model):
    CATEGORIA_CHOICES = [
        ("INFANTIL", "Infantil"),
        ("JUVENIL", "Juvenil"),
        ("ADULTO", "Adulto")
    ]
    LOCALIZACAO_CHOICES = [
        ('000', 'Generalidades'),
        ('100', 'Filosofia e Psicologia'),
        ('200', 'Religião'),
        ('300', 'Ciências sociais'),
        ('400', 'Língua e Linguagem'),
        ('500', 'Ciências Puras'),
        ('600', 'Tecnologia e ciências aplicadas'),
        ('700', 'Artes/Esportes e Recreação'),
        ('800', 'Literatura'),
        ('900', 'Geografia/História/Biografia'),
    ]
    
    titulo_livro = models.CharField(max_length=100)
    nome_autor = models.CharField(max_length=75)
    editora = models.CharField(max_length=50)
    genero = models.ManyToManyField(Genero)
    localizacao = models.CharField(max_length=3, choices=LOCALIZACAO_CHOICES)
    categoria = models.CharField(max_length=10, choices=CATEGORIA_CHOICES)
    sinopse = models.TextField(max_length=512)
    src_imagem = models.TextField()
    
    @classmethod
    def get_categorias(cls):
        return cls.CATEGORIA_CHOICES
    
    @classmethod
    def get_localizacao(cls):
        return cls.LOCALIZACAO_CHOICES 
       
    @classmethod
    def get_livros(cls):
        return cls.objects.all()
    @classmethod
    def get_livros_emprestados(cls):
        return [o.fk_livro for o in Emprestimo.objects.all()]    
    def get_generos_livro(self):
        return [genero.tipo_genero for genero in self.genero.all()]
    def get_localizacao_livro(self):
        localizacao = self.localizacao
        return [list(local) for local in Livro.LOCALIZACAO_CHOICES if local[0]==localizacao]

    @classmethod
    def get_livros_disponiveis(cls):
        id_livros_emprestados = [l.pk for l in Livro.get_livros_emprestados()]
        return [l for l in cls.objects.all().exclude(id__in=id_livros_emprestados)]

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
    
    def __str__(self) -> str:
        return f"{self.nome_autor} - {self.titulo_livro}"
    
    class Meta():
        db_table = 'livro'
        ordering = ['titulo_livro']
        
        
class Emprestimo(models.Model):    
    # Data atual
    hoje = datetime.date.today()
    DIAS_MES = 31
    # Adição de 2 meses a data atual
    daqui_2_meses = hoje + datetime.timedelta(days=DIAS_MES * 2)

    fk_user = models.OneToOneField(Usuario, blank=False, null=False, on_delete=models.RESTRICT)
    fk_livro = models.OneToOneField(Livro, blank=False, null=False, on_delete=models.RESTRICT)
    data_emprestimo = models.DateField(default=hoje)
    prazo_devolucao = models.DateField(default=daqui_2_meses)
    
    def tempo_ate_devolucao(self):
        return (self.prazo_devolucao - self.data_emprestimo)
    
    def __str__(self) -> str:
        return f"Empréstimo: {self.pk}. Devolução: {self.prazo_devolucao}. Tempo até devolução: {self.tempo_ate_devolucao()}"
    
    class Meta():
        db_table = 'emprestimo'
        ordering = ['data_emprestimo']
