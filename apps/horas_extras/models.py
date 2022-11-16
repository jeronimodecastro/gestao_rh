from django.db import models
from django.urls import reverse

from apps.funcionarios.models import Funcionario


class HoraExtra(models.Model):
    motivo = models.CharField(max_length=100)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.PROTECT)
    horas = models.DecimalField(max_digits=5, decimal_places=3)
    utilizada = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('list_horas_extras')
        # return reverse('update_hora_extra', args=[self.id])
        # return reverse('update_funcionario', args=[self.funcionario.id])

    def __str__(self):
        return self.motivo
