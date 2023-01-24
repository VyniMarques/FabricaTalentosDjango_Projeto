# Generated by Django 3.1.1 on 2023-01-24 19:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('aluno', '0001_initial'),
        ('disciplina', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Matricula',
            fields=[
                ('id', models.IntegerField(editable=True, primary_key=True, serialize=False)),
                ('np1', models.IntegerField(blank=True, null=True)),
                ('np2', models.IntegerField(blank=True, null=True)),
                ('np3', models.IntegerField(blank=True, null=True)),
                ('npa', models.IntegerField(blank=True, null=True)),
                ('alunos_ra', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='aluno.aluno')),
                ('disciplina_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='disciplina.disciplina')),
            ],
        ),
    ]
