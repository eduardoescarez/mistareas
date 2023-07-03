from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Modelo de los estados de las tareas
class Estados(models.Model):
    estado            = models.CharField(max_length=20, null=False, blank=False)

    def __str__(self):
        return self.estado

# Modelos de las etiquetas de las tareas
class Etiquetas(models.Model):
    etiqueta          = models.CharField(max_length=20, null=False, blank=False)

    def __str__(self):
        return self.etiqueta

# Modelo de las tareas
# Advertencia: Si se eliminan un usuario, todas sus tareas son eliminadas inmediatamente
class Tareas(models.Model):
    titulo            = models.CharField(max_length=45, null=False, blank=False)
    descripcion       = models.CharField(max_length=100, null=True, blank=True)
    fecha_creacion    = models.DateTimeField(default=timezone.now)
    fecha_modifica    = models.DateTimeField(auto_now=True)
    fecha_vencimiento = models.DateTimeField
    id_estado         = models.ForeignKey(Estados, on_delete=models.DO_NOTHING, null=False, blank=False)
    id_etiqueta       = models.ForeignKey(Etiquetas, on_delete=models.DO_NOTHING, null=False, blank=False)
    id_User           = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return self.titulo

