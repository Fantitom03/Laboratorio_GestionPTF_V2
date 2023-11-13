from django.shortcuts import render, redirect, reverse
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
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

class MiembrosTE_Detail(DetailView):
    model = Miembro_TE
    template_name = 'TE/miembroTE_detalle.html'


class MiembrosTE_Eliminar(DeleteView):
    model = Miembro_TE
    success_url = reverse_lazy('comision:miembroTE_list')


class MiembrosTE_Editar(UpdateView):
    model = Miembro_TE
    form_class = MiembroTE_Form
    template_name = 'TE/miembroTE_crear.html'
    success_url = reverse_lazy('comision:miembroTE_list')













