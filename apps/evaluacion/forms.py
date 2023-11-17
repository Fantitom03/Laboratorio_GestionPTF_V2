from django import forms
from django.core.exceptions import ValidationError
from .models import EvaluacionITF, EvaluacionPTF, Defensa
from datetime import date

class EvaluacionPTF_Form(forms.ModelForm):
    class Meta:
        model = EvaluacionPTF
        fields = [
            'evaluador',
            'proyecto_TF',
            'informe',
            'fecha_evaluacion',
            'estado',
            'observaciones',
        ]
        labels = {
            'evaluador':'Evaluador',
            'proyecto_TF':'Proyecto TF',
            'informe': 'Informe de Evaluacion',
            'fecha_evaluacion': 'Fecha de Evaluacion',
            'estado': 'Estado',
            'observaciones': 'Observaciones',
        }

    def clean_fecha_evaluacion(self):
        fecha_evaluacion = self.cleaned_data['fecha_evaluacion']

        # Verifica que la fecha_evaluacion no sea en el futuro
        if fecha_evaluacion and fecha_evaluacion > date.today():
            raise ValidationError("La fecha de evaluación no puede estar en el futuro.")

        return fecha_evaluacion

class EvaluacionITF_Form(forms.ModelForm):
    class Meta:
        model = EvaluacionITF
        fields = [
            'informe_TF',
            'informe',
            'fecha_evaluacion',
            'estado',
            'observaciones',
        ]
        labels = {
            'informe_TF':'ITF',
            'informe':'Informe de ITF',
            'fecha_evaluacion': 'Fecha de Evaluacion',
            'estado': 'Estado',
            'observaciones':'Observaciones',
        }

    def clean_fecha_evaluacion(self):
        fecha_evaluacion = self.cleaned_data['fecha_evaluacion']

        # Verifica que la fecha_evaluacion no sea en el futuro
        if fecha_evaluacion and fecha_evaluacion > date.today():
            raise ValidationError("La fecha de evaluación no puede estar en el futuro.")

        return fecha_evaluacion

class Defensa_Form(forms.ModelForm):
    class Meta:
        model = Defensa
        fields = [
            'informe_TF',
            'informe',
            'fecha_evaluacion',
            'estado',
        ]
        labels = {
            'informe_TF': 'ITF',
            'informe':'Informe de defensa',
            'fecha_evaluacion':'Fecha de Evaluacion',
            'estado': 'Estado',
        }

    def clean_fecha_evaluacion(self):
        fecha_evaluacion = self.cleaned_data['fecha_evaluacion']

        # Verifica que la fecha_evaluacion no sea en el futuro
        if fecha_evaluacion and fecha_evaluacion > date.today():
            raise ValidationError("La fecha de evaluación no puede estar en el futuro.")

        return fecha_evaluacion