from django import forms
from .models import Proyecto_TF, Proyecto_TF_Alumno, Informe_TF
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from datetime import datetime

class Proyecto_TF_AlumnoForm(forms.ModelForm):
    class Meta:
        model = Proyecto_TF_Alumno
        fields = (
            'proyecto_tf',
            'alumno'
        )


class Proyecto_TF_Form(forms.ModelForm):
    class Meta:
        model = Proyecto_TF
        fields = (
            'fecha_presentacion',
            'director',
            'co_director',
            'asesor',
            'titulo_ptf',
            'descripcion',
            'archivos_adjuntos',
            'certificado_analitico',
            'nota_aceptacion_director',
            'cstf',
            'te_asignado'
        )
        labels = {
            'fecha_presentacion': 'Fecha de presentación',
            'director': 'Director',
            'co_director': 'Co-director',
            'asesor': 'Asesor',
            'titulo_ptf': 'Título del PTF',
            'descripcion': 'Descripción del PTF',
            'archivos_adjuntos': 'Archivos adjuntos',
            'certificado_analitico': 'Certificado analítico',
            'nota_aceptacion_director': 'Nota de aceptación del director',
            'cstf': 'CSTF',
            'te_asignado': 'TE asignado',
        }
        widgets = {
            'fecha_presentacion': forms.DateInput(attrs={'type': 'date'}),
        }


    def clean_fecha_presentacion(self):
        fecha_presentacion = self.cleaned_data.get('fecha_presentacion')

        if fecha_presentacion and fecha_presentacion > datetime.now().date():
            raise ValidationError(_('La fecha de presentación no puede ser en el futuro.'))

        return fecha_presentacion


class Informe_TF_Form(forms.ModelForm):
    class Meta:
        model = Informe_TF
        fields = ('alumno', 'archivo_itf', 'proyecto_tf')