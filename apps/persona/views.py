from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView

from .models import Persona, Alumno, Docente, Asesor
from .forms import AlumnoForm

class AlumnoList (ListView):
    model = Alumno
    template_name = "alumno_list.html"

class AlumnoCreate (CreateView):
    model = Alumno
    form_class = AlumnoForm
    template_name = "alumno_create.hmtl"
    success_url = reverse_lazy ('persona: alumno_list')
