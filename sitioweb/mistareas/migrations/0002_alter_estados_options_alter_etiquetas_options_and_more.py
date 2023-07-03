# Generated by Django 4.2.2 on 2023-07-03 05:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mistareas', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='estados',
            options={'verbose_name': 'Estado', 'verbose_name_plural': 'Estados'},
        ),
        migrations.AlterModelOptions(
            name='etiquetas',
            options={'verbose_name': 'Etiqueta', 'verbose_name_plural': 'Etiquetas'},
        ),
        migrations.AlterModelOptions(
            name='tareas',
            options={'verbose_name': 'Tarea', 'verbose_name_plural': 'Tareas'},
        ),
        migrations.AddField(
            model_name='tareas',
            name='fecha_vencimiento',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]