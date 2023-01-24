# Generated by Django 3.1.1 on 2023-01-24 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estagio',
            fields=[
                ('id', models.IntegerField(editable=True, primary_key=True, serialize=False)),
                ('nome_empresa', models.CharField(max_length=45)),
                ('cnpj_empresa', models.CharField(max_length=18)),
                ('carga_horaria', models.IntegerField()),
            ],
        ),
    ]
