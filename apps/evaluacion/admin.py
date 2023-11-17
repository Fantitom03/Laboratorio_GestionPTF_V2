from django.contrib import admin
from apps.evaluacion.models import EvaluacionITF, EvaluacionPTF



@admin.register(EvaluacionPTF)
class EvaluacionPTFAdmin(admin.ModelAdmin):
    list_display = ('evaluador', 'proyecto_TF', 'informe', 'fecha_evaluacion', 'estado', 'observaciones')


@admin.register(EvaluacionITF)
class EvaluacionITFAdmin(admin.ModelAdmin):
    list_display = ('evaluador', 'informe_TF', 'informe', 'fecha_evaluacion', 'estado', 'observaciones')



