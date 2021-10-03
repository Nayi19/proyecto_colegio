from django.urls import path, include

from rest_framework.routers import DefaultRouter

from Usuarios.views import *

router = DefaultRouter()
router.register('usuarios', UsuarioAPI)

urlpatterns = [
    path('crud/', include(router.urls))
]