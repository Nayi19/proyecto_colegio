from rest_framework import fields, serializers

from asignaturas.models import *

class CienciaSerial (serializers.ModelSerializer):
    class Meta:
        model = Ciencia_y_Tecnología
        fields = '__all__'


class ConvivenciaSerial (serializers.ModelSerializer):
    class Meta:
        model = Convivencia_y_Sociedad
        fields = '__all__'


class ComunicacionSerial (serializers.ModelSerializer):
    class Meta:
        model = Comunicación_y_lenguaje
        fields = '__all__'


