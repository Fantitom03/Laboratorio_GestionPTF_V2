from django import forms
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



class MiembroTE_Form(forms.ModelForm):
    class Meta:
        model = Miembro_TE
        fields = (
            'docente',
            'rol',
            'fecha_alta'
        )
        labels = {
            'docente': 'Docente',
            'rol': 'ROL',
            'fecha_alta': 'FECHA ALTA'

        }

        widgets = {
            'fecha_alta' : forms.DateInput(attrs={'class' : 'form-control'})

        }

class TribunalEvaluadorForm(forms.ModelForm):
    class Meta:
        model = TribunalEvaluador
        fields = (
            'numero_disposicion',
            'fecha_disposicion',
            'archivo_disposicion',
            'miembros'
        )

    miembros = forms.ModelChoiceField(
        queryset=Docente.objects.all(),
        empty_label='Seleccione un docente',  # Etiqueta para la opción por defecto
        #help_text='Seleccione un docente para agregar al Tribunal Evaluador.',
        required=False
    )

