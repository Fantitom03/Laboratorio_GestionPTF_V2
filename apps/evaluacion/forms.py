from django import forms
from .models import EvaluacionITF, EvaluacionPTF, Defensa

class EvaluacionPTF_Form (forms.ModelForm):
    model = EvaluacionPTF
    fields = [
        'proyecto_TF',
        'informe',
        'fecha_evaluacion',
        'estado',
        'observaciones',
    ]
    labels = {
        'proyecto_TF':'Proyecto TF',
        'informe': 'Informe de Evaluacion',
        'fecha_evaluacion': 'Fecha de Evaluacion',
        'estado': 'Estado',
        'observaciones': 'Observaciones',
    }

class EvaluacionITF_Form (forms.ModelForm):
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

class Defensa_Form (forms.ModelForm):
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