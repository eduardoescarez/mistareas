from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Modelo de los estados de las tareas
class Estados(models.Model):
    estado            = models.CharField(max_length=20, null=False, blank=False, verbose_name='Estado')

    class Meta:
        verbose_name = 'Estado'
        verbose_name_plural = 'Estados'


    def __str__(self):
        return self.estado

# Modelos de las etiquetas de las tareas
class Etiquetas(models.Model):
    etiqueta          = models.CharField(max_length=20, null=False, blank=False, verbose_name='Etiqueta')

    class Meta:
        verbose_name = 'Etiqueta'
        verbose_name_plural = 'Etiquetas'


    def __str__(self):
        return self.etiqueta

# Modelos de las prioridades de las tareas
class Prioridades(models.Model):
    prioridad          = models.CharField(max_length=20, null=False, blank=False, verbose_name='Etiqueta')

    class Meta:
        verbose_name = 'Prioridad'
        verbose_name_plural = 'prioridades'


    def __str__(self):
        return self.prioridad

# Modelo de las tareas
# Advertencia: Si se eliminan un usuario, todas sus tareas son eliminadas inmediatamente
class Tareas(models.Model):
    titulo            = models.CharField(max_length=45, null=False, blank=False, verbose_name='Titulo')
    descripcion       = models.CharField(max_length=200, null=True, blank=True, verbose_name='Descripción')
    fecha_creacion    = models.DateTimeField(default=timezone.now, verbose_name='Fecha de creación')
    fecha_modifica    = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')
    fecha_vencimiento = models.DateTimeField(default=timezone.now, verbose_name='Fecha de vencimiento')
    id_estado         = models.ForeignKey(Estados, on_delete=models.DO_NOTHING, null=False, blank=False, verbose_name='Estado')
    id_etiqueta       = models.ForeignKey(Etiquetas, on_delete=models.DO_NOTHING, null=False, blank=False, verbose_name='Etiqueta')
    id_prioridad      = models.ForeignKey(Prioridades, on_delete=models.DO_NOTHING, null=False, blank=False, verbose_name='Prioridad', default=1)
    id_User           = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False, verbose_name='Usuario')
    observaciones     = models.CharField(max_length=200, null=True, blank=True, verbose_name='Observaciones')

    class Meta:
        verbose_name = 'Tarea'
        verbose_name_plural = 'Tareas'

    def __str__(self):
        return self.titulo