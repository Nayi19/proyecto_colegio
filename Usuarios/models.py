from django.db import models

from django.contrib.auth import get_user_model


#from Asignaturas import *

class Perfil (models.Model):
    usuario = models.ForeignKey (get_user_model(), on_delete=models.CASCADE)
    nombre = models.CharField (max_length=200)
    apellido = models.CharField (max_length=200)
    direccion = models.CharField (max_length=200)
    telefono = models.CharField (max_length=200)
    edad = models.IntegerField (blank=False)

    def __str__(self):
        return self.nombre+' '+self.apellido

class docente (models.Model):
    nombre= models.ForeignKey(Perfil, on_delete=models.CASCADE)
    #asignatura= models.ForeignKey(materias, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nombre