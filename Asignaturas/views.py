from rest_framework import viewsets

from Asignaturas.serializers import *


class MateriaAPI (viewsets.ModelViewSet):
    serializer_class = MateSerial
    queryset = materias.objects.all()



    
