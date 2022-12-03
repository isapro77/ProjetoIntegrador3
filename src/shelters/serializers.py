from rest_framework import serializers

from .models import *


class ShelterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shelter
        fields = (
            "nome",
            "endereço",
            "pet",
        )

