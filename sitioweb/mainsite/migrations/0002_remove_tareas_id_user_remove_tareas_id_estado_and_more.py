# Generated by Django 4.2.2 on 2023-07-03 05:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tareas',
            name='id_User',
        ),
        migrations.RemoveField(
            model_name='tareas',
            name='id_estado',
        ),
        migrations.RemoveField(
            model_name='tareas',
            name='id_etiqueta',
        ),
        migrations.DeleteModel(
            name='Estados',
        ),
        migrations.DeleteModel(
            name='Etiquetas',
        ),
        migrations.DeleteModel(
            name='Tareas',
        ),
    ]