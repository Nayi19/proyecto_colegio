from rest_framework import viewsets

from Historial.serializers import *


class ObservadorAPI (viewsets.ModelViewSet):
    serializer_class = ObservSerial
    queryset = observador.objects.all()

