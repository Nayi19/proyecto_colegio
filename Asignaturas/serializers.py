from rest_framework import fields, serializers

from Asignaturas.models import *

class MateSerial (serializers.ModelSerializer):
    class Meta:
        model = materias
        fields = '__all__'




