from django.urls import path,include
from rest_framework import routers, urlpatterns

from asignaturas.views import *

from rest_framework.routers import DefaultRouter
#localhost:8000/asignaturas/api/crud/ciencia
#localhost:8000/asignaturas/api/crud/convivencia

router = DefaultRouter()

router.register('ciencia', CienciaAPI)
router.register('convivencia', ConvivenciaAPI)
router.register('comunicacion',ComunicacionAPI)

urlpatterns = [
    path ('crud/', include(router.urls))
]
