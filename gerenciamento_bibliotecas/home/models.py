from django.db import models

# Create your models here.
class Genero(models.Model):
    tipo_genero = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return f"{self.tipo_genero}"
    
    class Meta():
        db_table = 'genero'
        ordering = ['tipo_genero']
