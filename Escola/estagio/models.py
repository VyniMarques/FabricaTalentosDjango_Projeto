from django.db import models


class Estagio(models.Model):
    id = models.IntegerField(primary_key=True, editable=True)
    nome_empresa = models.CharField(max_length=45)
    cnpj_empresa = models.CharField(max_length=18)
    carga_horaria = models.IntegerField()
