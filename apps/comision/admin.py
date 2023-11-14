from django.contrib import admin
from apps.comision.models import Miembro_CSTF, Miembro_TE, TribunalEvaluador


@admin.register(Miembro_TE)
class MiembroTEAdmin(admin.ModelAdmin):
    list_display = ('docente', 'rol', 'fecha_alta')


@admin.register(Miembro_CSTF)
class MiembroCSTFAdmin(admin.ModelAdmin):
    list_display = ('docente', 'resolucion_asignacion', 'fecha_alta')


