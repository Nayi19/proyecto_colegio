from rest_framework import fields, serializers

from Historial.models import *

class ObservSerial (serializers.ModelSerializer):
    class Meta:
        model = observador
        fields = '__all__'
