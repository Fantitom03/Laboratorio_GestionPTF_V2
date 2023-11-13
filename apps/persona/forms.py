from django import forms
from .models import Docente, Alumno, Asesor

class DocenteForm(forms.ModelForm):
    class Meta:
        model = Docente
        fields = ('dni', 'nombre', 'apellido', 'cuil')


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
        fields = ('dni', 'nombre', 'apellido', 'curriculum')