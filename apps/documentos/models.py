from django.db import models
from apps.funcionarios.models import Funcionario

class Documento(models.Model):
    descricao = models.CharField(max_length=100)
    funcionario = models.ForeignKey(Funcionario, models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.descricao
