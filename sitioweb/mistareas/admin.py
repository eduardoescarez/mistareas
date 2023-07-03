from django.contrib import admin
from mistareas.models import Estados, Etiquetas, Tareas

# Register your models here.

# Panel de administración de Estados
class EstadosAdmin(admin.ModelAdmin):
    list_display    = ['id', 'estado']
    ordering        = ['id']
    fields          = ['id', 'estado']
    readonly_fields = ['id']

# Panel de administración de Etiquetas
class EtiquetasAdmin(admin.ModelAdmin):
    list_display    = ['id', 'etiqueta']
    ordering        = ['id']
    fields          = ['id', 'etiqueta']
    readonly_fields = ['id']


# Panel de administración de Tareas
class TareasAdmin(admin.ModelAdmin):
    list_display    = ['id', 'titulo', 'id_User', 'fecha_creacion']
    ordering        = ['id']
    fields          = ['id', 'titulo', 'descripcion', 'id_estado', 'id_etiqueta', 'id_User', 'fecha_creacion', 'fecha_vencimiento']
    readonly_fields = ['id']

admin.site.register(Estados, EstadosAdmin)
admin.site.register(Etiquetas, EtiquetasAdmin)
admin.site.register(Tareas, TareasAdmin)