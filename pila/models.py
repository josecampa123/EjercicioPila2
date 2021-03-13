from django.db import models

# Create your models here.
class Pila(models.Model):
    marca = models.CharField(max_length=200)
    modelo = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    tipo = models.CharField(max_length=200)
    numLLantas = models.CharField(max_length=200)
    
    imagenes = models.ImageField(upload_to='imagenes', null=True)
 

    def __str__(self):
        return f'{self.marca} - {self.modelo} - {self.color} - {self.tipo} - {self.numLLantas}...'

    