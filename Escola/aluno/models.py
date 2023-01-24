from django.db import models

from estagio.models import Estagio


class Aluno(models.Model):
    ra = models.IntegerField(primary_key=True, editable=True)
    cpf = models.CharField(max_length=14)
    nome = models.CharField(max_length=45)
    ano_nascimento = models.IntegerField()
    cidade = models.CharField(max_length=45)
    bairro = models.CharField(max_length=45)
    rua = models.CharField(max_length=45)
    numero = models.IntegerField()
    complemento = models.CharField(max_length=200, blank=True, null=True)

    estagio_id = models.ForeignKey(Estagio, on_delete=models.CASCADE, blank=True, null=True)