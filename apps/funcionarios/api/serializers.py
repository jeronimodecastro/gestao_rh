from rest_framework import serializers
from apps.funcionarios.models import Funcionario
from apps.horas_extras.api.serializers import HoraExtraSerializer


class FuncionarioSerializer(serializers.ModelSerializer):
    horaextra_set = HoraExtraSerializer(many=True)

    class Meta:
        model = Funcionario
        fields = ['id', 'usuario', 'nome', 'departamentos', 'empresa', 'horaextra_set']
