from django.db import models


class Empresa(models.Model):
    nome = models.CharField(max_length=100, help_text="Cadastro de Empresas")