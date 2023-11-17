from django import forms
from .models import Proyecto_TF, Proyecto_TF_Alumno
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from datetime import datetime


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

class Proyecto_TF_AlumnoForm(forms.ModelForm):
    class Meta:
        model = Proyecto_TF_Alumno
        fields = ('proyecto_tf', 'alumno')


class Proyecto_TF_Form(forms.ModelForm):
    class Meta:
        model = Proyecto_TF
        fields = ('fecha_presentacion', 'director', 'co_director', 'asesor', 'titulo_ptf', 'descripcion', 'cstf', 'te_asignado')

    def clean_fecha_presentacion(self):
        fecha_presentacion = self.cleaned_data.get('fecha_presentacion')

        if fecha_presentacion and fecha_presentacion < datetime.now().date():
            raise ValidationError(_('La fecha de presentación no puede ser en el pasado.'))

        return fecha_presentacion

class Informe_TF_Form(forms.ModelForm):
    pass