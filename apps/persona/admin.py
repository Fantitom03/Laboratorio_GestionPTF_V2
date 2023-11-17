from django.contrib import admin
from apps.persona.models import Docente, Alumno, Persona, Asesor
from django.contrib.auth.models import Permission

@admin.register(Docente)
class DocenteAdmin(admin.ModelAdmin):
    list_display = ('dni', 'nombre', 'apellido', 'cuil')


@admin.register(Alumno)
class AlumnoAdmin(admin.ModelAdmin):
    model = Alumno
    permission = (
        ("persmiso_alumno", "Permiso_Alumno")
    )
    list_display = ('dni', 'nombre', 'apellido', 'matricula', 'correo_electronico')



admin.site.register(Asesor)

admin.site.register(Permission)



