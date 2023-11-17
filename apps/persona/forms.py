from django import forms
from .models import Docente, Alumno, Asesor

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = (
            'dni',
            'nombre',
            'apellido',
            'matricula',
            'correo_electronico'
        )
        labels = {
            'dni' : 'DNI',
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'matricula' : 'Matricula',
            'correo_electronico': 'Correo Electrónico',
        }


class AsesorForm(forms.ModelForm):
    class Meta:
        model = Asesor
        fields = (
            'dni',
            'nombre',
            'apellido',
            'curriculum'
        )
        labels = {
            'dni': 'DNI',
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'curriculum': 'Curriculum',
        }

class DocenteForm(forms.ModelForm):
    class Meta:
        model = Docente
        fields = [
            'dni',
            'cuil',
            'nombre',
            'apellido',
        ]
        labels = {
            'dni' : 'DNI',
            'cuil' : 'CUIL',
            'nombre' : 'Nombre',
            'apellido' : 'Apellido',
        }