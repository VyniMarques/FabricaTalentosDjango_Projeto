from disciplina.models import Disciplina
from aluno.models import Aluno
from django.db import models


class Matricula(models.Model):
    id = models.IntegerField(primary_key=True, editable=True)
    np1 = models.IntegerField(blank=True, null=True)
    np2 = models.IntegerField(blank=True, null=True)
    np3 = models.IntegerField(blank=True, null=True)
    npa = models.IntegerField(blank=True, null=True)

    alunos_ra = models.ForeignKey(Aluno, on_delete=models.CASCADE, blank=True, null=True)
    disciplina_id = models.ForeignKey(Disciplina, on_delete=models.CASCADE, blank=True, null=True)
