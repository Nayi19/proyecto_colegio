from typing import Text
from django.db import models

# Create your models here.
class materias (models.Model):
    nombre = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    grado = models.CharField(max_length=50)
    #profesor = models.ForeignKey()

    def __str__(self):
        return self.area + ' de ' + self.grado

