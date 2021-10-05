from django.urls import path, include
from rest_framework.routers import DefaultRouter

from Calificaciones.views import *

router = DefaultRouter()
router.register('notas', NotasAPI)


urlpatterns = [
    path('crud/', include(router.urls))
]