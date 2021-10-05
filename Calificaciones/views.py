from rest_framework import viewsets

from Calificaciones.serializers import *

class NotasAPI(viewsets.ModelViewSet):
    serializer_class = NotaSerial
    queryset = notas.objects.all()
