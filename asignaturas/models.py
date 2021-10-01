from typing import Text
from django.db import models

# Create your models here.
class Ciencia_y_Tecnología (models.Model):
    foto = models.ImageField(null=True, blank=True)
    area = models.CharField(max_length=100)
    grado = models.CharField(max_length=50)
    docente = models.CharField(max_length=200)

    def __str__(self):
        return self.area + ' de ' + self.grado

class Convivencia_y_Sociedad (models.Model):
    foto = models.ImageField(null=True, blank=True)
    area = models.CharField(max_length=100)
    grado = models.CharField(max_length=50)
    docente = models.CharField(max_length=200)

    def __str__(self):
        return self.area + ' de ' + self.grado

class Comunicación_y_lenguaje (models.Model):
    foto = models.ImageField(null=True, blank=True)
    area = models.CharField(max_length=100)
    grado = models.CharField(max_length=50)
    docente = models.CharField(max_length=200)

    def __str__(self):
        return self.area + ' de ' + self.grado