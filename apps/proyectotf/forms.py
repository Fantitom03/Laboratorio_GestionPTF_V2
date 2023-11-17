from django import forms
from .models import Proyecto_TF, Proyecto_TF_Alumno
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from datetime import datetime

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

