# Generated by Django 4.2.2 on 2023-07-05 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mistareas', '0003_alter_estados_estado_alter_etiquetas_etiqueta_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tareas',
            name='observaciones',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Observaciones'),
        ),
        migrations.AlterField(
            model_name='tareas',
            name='descripcion',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Descripción'),
        ),
    ]
