from rest_framework import serializers
from .models import Portico

class PorticoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Portico
        fields = ('id_portico', 'ubicacion')
