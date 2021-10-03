from django.urls import path,include
from rest_framework import routers, urlpatterns

from Asignaturas.views import *

from rest_framework.routers import DefaultRouter
#localhost:8000/asignaturas/api/crud/materia


router = DefaultRouter()

router.register('materia', MateriaAPI)

urlpatterns = [
    path ('crud/', include(router.urls))
]
