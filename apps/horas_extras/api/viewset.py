from rest_framework import viewsets
from apps.horas_extras.api.serializers import HoraExtraSerializer
from apps.horas_extras.models import HoraExtra
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


class HoraExtraViewSet(viewsets.ModelViewSet):
    queryset = HoraExtra.objects.all()
    serializer_class = HoraExtraSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )

    # Para autenticar passar o token no HTTP Header no padrão abaixo
    # Chave: Authorization
    # Valor: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b
    # Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b
