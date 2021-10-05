from typing import Text
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey

# Create your models here.
class observador (models.Model):
    educando = models.CharField(max_length=100)
    comentario = models.TextField()
    periodo = models.IntegerField(default=0)
    

    def __str__(self):
        return self.comentario + ' - periodo:  ' + self.periodo

