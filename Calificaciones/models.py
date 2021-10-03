from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey

from Asignaturas.models import materias

# Create your models here.
class notas(models.Model):
    materia = models.ForeignKey(materias, on_delete=CASCADE)
    cuantitativa = models.FloatField(default=0)
    cualitativa = models.CharField(max_length=200)
    estudiante = models.CharField(max_length=200)

    def __str__(self):
        return self.materia.nombre + " - " + self.materia.area + " - " + self.materia.grado + " - " + self.materia.profesor
