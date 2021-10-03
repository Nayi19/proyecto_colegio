from django.db.models.base import Model
from rest_framework import serializers

from Usuarios.models import *

class UserSerial (serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password']
        extra_kwargs = {
            'password': {
                'write_only':True,
                'style': {
                    'input_type': 'password'
                }
            }
        }

class PerfilSerial(serializers.ModelSerializer):
    class Meta:
        model = Perfil
        fields = '__all__'