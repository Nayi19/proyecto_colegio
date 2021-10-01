from rest_framework import viewsets

from asignaturas.serializers import *


class CienciaAPI (viewsets.ModelViewSet):
    serializer_class = CienciaSerial
    queryset = Ciencia_y_Tecnología.objects.all()


class ConvivenciaAPI (viewsets.ModelViewSet):
    serializer_class = ConvivenciaSerial
    queryset = Convivencia_y_Sociedad.objects.all()

class ComunicacionAPI (viewsets.ModelViewSet):
    serializer_class = ComunicacionSerial
    queryset = Comunicación_y_lenguaje.objects.all()


    
