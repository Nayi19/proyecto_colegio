from typing import Text
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey
#from Usuarios.models import *

# Create your models here.
class materias (models.Model):
    nombre = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    grado = models.CharField(max_length=50)
    #profesor = models.ForeignKey(docente, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nombre + ' de ' + self.grado

