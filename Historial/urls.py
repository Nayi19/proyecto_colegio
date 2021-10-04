from django.urls import path,include
from rest_framework import routers, urlpatterns

from Historial.views import *

from rest_framework.routers import DefaultRouter



router = DefaultRouter()

router.register('observador', ObservadorAPI)

urlpatterns = [
    path ('crud/', include(router.urls))
]
