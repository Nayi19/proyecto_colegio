from rest_framework import serializers

from Calificaciones.models import *

class NotaSerial(serializers.ModelSerializer):
    class Meta:
        model = notas
        fields = '__all__'
        #fields = ["nombre", "foto"]