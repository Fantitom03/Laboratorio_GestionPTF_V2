from django import forms
from .models import Proyecto_TF, Proyecto_TF_Alumno

class Proyecto_TF_AlumnoForm(forms.ModelForm):
    class Meta:
        model = Proyecto_TF_Alumno
        fields = ('proyecto_tf', 'alumno')


class Proyecto_TF_Form(forms.ModelForm):
    class Meta:
        model = Proyecto_TF
        fields = ('fecha_presentacion', 'director', 'co_director', 'asesor', 'titulo_ptf', 'descripcion', 'cstf', 'te_asignado')


