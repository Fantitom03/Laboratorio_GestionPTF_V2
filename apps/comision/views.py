from django.shortcuts import render, redirect, reverse
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy

from apps.comision.forms import MiembroTE_Form,  Miembro_CSTF_Form, TribunalEvaluadorForm
from apps.comision.models import Miembro_TE, Miembro_CSTF

class MiembrosTE_List(ListView):
    model = Miembro_TE
    template_name = 'TE/miembroTE_list.html'

class MiembrosTE_Create(CreateView):
    model = Miembro_TE
    form_class = MiembroTE_Form
    template_name = 'TE/miembroTE_crear.html'
    success_url = reverse_lazy('comision:miembroTE_list')