from django import forms
from .models import Miembro_CSTF, Miembro_TE, TribunalEvaluador
from apps.persona.models import Docente
class Miembro_CSTF_Form(forms.ModelForm):
    class Meta:
        model = Miembro_CSTF
        fields = ('docente', 'resolucion_asignacion', 'fecha_alta')

class Miembro_TE_Form(forms.ModelForm):
    class Meta:
        model = Miembro_TE
        fields = ('docente', 'rol', 'fecha_alta')

class TribunalEvaluadorForm(forms.ModelForm):
    class Meta:
        model = TribunalEvaluador
        fields = ('numero_disposicion', 'fecha_disposicion', 'archivo_disposicion', 'miembros')


    miembros = forms.ModelMultipleChoiceField(
        queryset = Docente.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )