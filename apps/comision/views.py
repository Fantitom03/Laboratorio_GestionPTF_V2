from django.shortcuts import render, redirect
from django.views.generic import ListView

from apps.comision.forms import Miembro_TE_Form,  Miembro_CSTF_Form, TribunalEvaluadorForm
from apps.comision.models import Miembro_TE, Miembro_CSTF

class MiembrosTE_List(ListView):
    model = Miembro_TE
    template_name = 'comision/miembroTE_list.html'