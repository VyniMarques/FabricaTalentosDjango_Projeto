from django.db import models


class Disciplina(models.Model):
    id = models.IntegerField(primary_key=True, editable=True)
    nome = models.CharField(max_length=45)
    conteudo = models.CharField(max_length=300)
    carga_horaria = models.IntegerField()
