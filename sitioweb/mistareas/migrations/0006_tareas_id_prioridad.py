# Generated by Django 4.2.2 on 2023-07-07 06:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mistareas', '0005_prioridades'),
    ]

    operations = [
        migrations.AddField(
            model_name='tareas',
            name='id_prioridad',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='mistareas.prioridades', verbose_name='Prioridad'),
        ),
    ]