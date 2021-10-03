from django.db import models

# Create your models here.
from django.contrib.auth import get_user_model

class Perfil (models.Model):
    usuario = models.ForeignKey (get_user_model(), on_delete=models.CASCADE)
    nombre = models.CharField (max_length=200)
    apellido = models.CharField (max_length=200)
    direccion = models.CharField (max_length=200)
    telefono = models.CharField (max_length=200)
    edad = models.IntegerField (blank=False)

    def __str__(self):
        return self.nombre+' '+self.apellido