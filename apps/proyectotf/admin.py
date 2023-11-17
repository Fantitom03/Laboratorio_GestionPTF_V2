from django.contrib import admin
from apps.proyectotf.models import Proyecto_TF, Informe_TF, Proyecto_TF_Alumno


@admin.register(Proyecto_TF)
class Proyecto_TFAdmin(admin.ModelAdmin):
    list_display = ('fecha_presentacion', 'director', 'co_director', 'asesor', 'titulo_ptf', 'descripcion', 'estado', 'observaciones', 'cstf', 'te_asignado')


@admin.register(Informe_TF)
class Informe_TFAdmin(admin.ModelAdmin):
    list_display = ('alumno', 'archivo_itf', 'proyecto_tf', 'estado', 'observaciones')


@admin.register(Proyecto_TF_Alumno)
class Proyecto_TF_AlumnoAdmin(admin.ModelAdmin):
    list_display = ('proyecto_tf', 'alumno')

