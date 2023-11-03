from django.contrib import admin
from apps.persona.models import Docente, Alumno, Persona, Asesor

@admin.register(Docente)
class DocenteAdmin(admin.ModelAdmin):
    list_display = ('dni', 'nombre', 'apellido', 'cuil')


@admin.register(Alumno)
class AlumnoAdmin(admin.ModelAdmin):
    list_display = ('dni', 'nombre', 'apellido', 'matricula', 'correo_electronico')

