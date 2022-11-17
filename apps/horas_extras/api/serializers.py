from rest_framework import serializers
from apps.horas_extras.models import HoraExtra


class HoraExtraSerializer(serializers.ModelSerializer):
    class Meta:
        model = HoraExtra
        fields = ['id', 'motivo', 'funcionario', 'horas', 'utilizada']
