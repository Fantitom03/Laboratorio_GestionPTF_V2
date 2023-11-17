from django import forms
from django.core.exceptions import ValidationError
from .models import Docente, Alumno, Asesor
import  re

class CustomForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CustomForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            # Agregar una clase CSS a cada campo del formulario
            field.widget.attrs['class'] = 'form-control'

    def add_error(self, field, error):
        # Personalizar el mensaje de error agregando una clase CSS
        super().add_error(field, error)
        self.fields[field].widget.attrs.update({'class': 'form-control is-invalid'})

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = (
            'dni',
            'nombre',
            'apellido',
            'matricula',
            'correo_electronico',
            'crear_usuario',
        )
        labels = {
            'dni' : 'DNI',
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'matricula' : 'Matricula',
            'correo_electronico': 'Correo Electrónico',
            'crear_usuario': 'Crear Usuario',
        }

    def clean_dni(self):
        dni = self.cleaned_data['dni']

        # Verifica la longitud del DNI
        if len(dni) != 8:
            raise ValidationError("El DNI debe tener 8 dígitos.")

        return dni

    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
        # Verifica que el nombre solo contenga letras y espacios
        if not re.match('^[a-zA-Z ]+$', nombre):
            raise ValidationError("El nombre solo debe contener letras y espacios.")
        return nombre

    def clean_apellido(self):
        apellido = self.cleaned_data['apellido']
        # Verifica que el apellido solo contenga letras y espacios
        if not re.match('^[a-zA-Z ]+$', apellido):
            raise ValidationError("El apellido solo debe contener letras y espacios.")
        return apellido

    def clean_matricula(self):
        matricula = self.cleaned_data['matricula']

        # Verifica que la matricula solo contenga números
        if not matricula.isdigit():
            raise ValidationError("La matricula debe contener solo números.")

        return matricula

    def clean_crear_usuario(self):
        crear_usuario = self.cleaned_data['crear_usuario']

        # Verifica que el campo crear_usuario sea un booleano
        if not isinstance(crear_usuario, bool):
            raise ValidationError("El campo crear_usuario debe ser un booleano.")

        return crear_usuario

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
        fields = (
            'dni',
            'nombre',
            'apellido',
            'cuil',
            'correo_electronico',
            'crear_usuario',
        )
        labels = {
            'dni': 'DNI',
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'cuil': 'Cuil',
            'correo_electronico': 'Correo Electrónico',
            'crear_usuario': 'Crear Usuario',
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

    def clean_crear_usuario(self):
        crear_usuario = self.cleaned_data['crear_usuario']

        # Verifica que el campo crear_usuario sea un booleano
        if not isinstance(crear_usuario, bool):
            raise ValidationError("El campo crear_usuario debe ser un booleano.")

        return crear_usuario