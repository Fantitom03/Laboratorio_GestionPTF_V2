from datetime import date

from django import forms
from django.core.exceptions import ValidationError

from .models import Miembro_CSTF, Miembro_TE, TribunalEvaluador
from apps.persona.models import Docente
class Miembro_CSTF_Form(forms.ModelForm):
    class Meta:
        model = Miembro_CSTF
        fields = (
            'docente',
            'resolucion_asignacion',
            'fecha_alta'
        )

    labels = {
        'docente': 'Docente',
        'resolucion_asignacion':'Resolucion Asignacion',
        'fecha_alta':'Fecha de Alta',
    }

    widgets = {
        'fecha_alta': forms.DateInput(attrs={'type': 'date'}),
    }

    def clean_fecha_evaluacion(self):
        fecha_alta = self.cleaned_data['fecha_alta']

        # Verifica que la fecha_evaluacion no sea en el futuro
        if fecha_alta and fecha_alta > date.today():
            raise ValidationError("La fecha de alta no puede estar en el futuro.")

        return fecha_alta

class Miembro_TE_Form(forms.ModelForm):
    class Meta:
        model = Miembro_TE
        fields = (
            'docente',
            'rol',
            'fecha_alta'
        )

    labels = {
        'docente': 'Docente',
        'rol': 'Rol',
        'fecha_alta': 'Fecha de Alta',
    }

    widgets = {
        'fecha_alta': forms.DateInput(attrs={'type': 'date'}),
    }

    def clean_fecha_evaluacion(self):
        fecha_alta = self.cleaned_data['fecha_alta']

        # Verifica que la fecha_evaluacion no sea en el futuro
        if fecha_alta and fecha_alta > date.today():
            raise ValidationError("La fecha de alta no puede estar en el futuro.")

        return fecha_alta



class TribunalEvaluadorForm(forms.ModelForm):
    class Meta:
        model = TribunalEvaluador
        fields = (
            'numero_disposicion',
            'fecha_disposicion',
            'archivo_disposicion')

    labels = {
        'numero_disposicion': 'Numero de Disposicion',
        'fecha_disposicion': 'Fecha de Disposicion',
        'archivo_disposicion': 'Archivo de Disposicion',
    }

    widgets = {
        'fecha_disposicion': forms.DateInput(attrs={'type': 'date'}),
    }

    def clean_fecha_evaluacion(self):
        fecha_disposicion = self.cleaned_data['fecha_disposicion']

        # Verifica que la fecha_evaluacion no sea en el futuro
        if fecha_disposicion and fecha_disposicion > date.today():
            raise ValidationError("La fecha de disposicion no puede estar en el futuro.")

        return fecha_disposicion



