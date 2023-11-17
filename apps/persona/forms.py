from django import forms
from django.core.exceptions import ValidationError
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

    def clean_dni(self):
        dni = self.cleaned_data['dni']

        # Verifica la longitud del DNI
        if len(dni) != 8:
            raise ValidationError("El DNI debe tener 8 dígitos.")

        return dni

    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']

        # Verifica que el nombre solo contenga letras
        if not nombre.isalpha():
            raise ValidationError("El nombre debe contener solo letras.")

        return nombre

    def clean_apellido(self):
        apellido = self.cleaned_data['apellido']

        # Verifica que el apellido solo contenga letras
        if not apellido.isalpha():
            raise ValidationError("El apellido debe contener solo letras.")

        return apellido

    def clean_matricula(self):
        matricula = self.cleaned_data['matricula']

        # Verifica que la matricula solo contenga números
        if not matricula.isdigit():
            raise ValidationError("La matricula debe contener solo números.")

        return matricula

    # Agrega métodos clean adicionales para otros campos según sea necesario

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

    def clean_dni(self):
        dni = self.cleaned_data['dni']

        # Verifica la longitud del DNI
        if len(dni) != 8:
            raise ValidationError("El DNI debe tener 8 dígitos.")

        return dni

    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']

        # Verifica que el nombre solo contenga letras
        if not nombre.isalpha():
            raise ValidationError("El nombre debe contener solo letras.")

        return nombre

    def clean_apellido(self):
        apellido = self.cleaned_data['apellido']

        # Verifica que el apellido solo contenga letras
        if not apellido.isalpha():
            raise ValidationError("El apellido debe contener solo letras.")

        return apellido

    # Agrega métodos clean adicionales para otros campos según sea necesario

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

    def clean_dni(self):
        dni = self.cleaned_data['dni']

        # Verifica la longitud del DNI
        if len(dni) != 8:
            raise ValidationError("El DNI debe tener 8 dígitos.")

        return dni

    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']

        # Verifica que el nombre solo contenga letras
        if not nombre.isalpha():
            raise ValidationError("El nombre debe contener solo letras.")

        return nombre

    def clean_apellido(self):
        apellido = self.cleaned_data['apellido']

        # Verifica que el apellido solo contenga letras
        if not apellido.isalpha():
            raise ValidationError("El apellido debe contener solo letras.")

        return apellido

    def clean_cuil(self):
        cuil = self.cleaned_data['cuil']

        # Verifica que el CUIL solo contenga números
        if not cuil.isdigit():
            raise ValidationError("El CUIL debe contener solo números.")

        return cuil