from django import forms
from django.core.exceptions import ValidationError
from .models import Miembro_CSTF, Miembro_TE, TribunalEvaluador
from apps.persona.models import Docente
from datetime import date

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

class Miembro_CSTF_Form(forms.ModelForm):
    class Meta:
        model = Miembro_CSTF
        fields = ('docente', 'resolucion_asignacion', 'fecha_alta')

    def clean_fecha_alta(self):
        fecha_alta = self.cleaned_data['fecha_alta']

        # Verifica que la fecha_alta no sea en el futuro
        if fecha_alta and fecha_alta > date.today():
            raise ValidationError("La fecha de alta no puede estar en el futuro.")

        return fecha_alta

class Miembro_TE_Form(forms.ModelForm):
    class Meta:
        model = Miembro_TE
        fields = ('docente', 'rol', 'fecha_alta')

    def clean_fecha_alta(self):
        fecha_alta = self.cleaned_data['fecha_alta']

        # Verifica que la fecha_alta no sea en el futuro
        if fecha_alta and fecha_alta > date.today():
            raise ValidationError("La fecha de alta no puede estar en el futuro.")

        return fecha_alta

class TribunalEvaluadorForm(forms.ModelForm):
    class Meta:
        model = TribunalEvaluador
        fields = ('numero_disposicion', 'fecha_disposicion', 'archivo_disposicion')

    def clean_fecha_disposicion(self):
        fecha_disposicion = self.cleaned_data['fecha_disposicion']

        # Verifica que la fecha_disposicion no sea en el futuro
        if fecha_disposicion and fecha_disposicion > date.today():
            raise ValidationError("La fecha de disposición no puede estar en el futuro.")

        return fecha_disposicion