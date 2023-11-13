from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from django.contrib.auth import authenticate, login, logout

from .models import Persona, Alumno, Docente, Asesor
from .forms import AlumnoForm

class AlumnoList (ListView):
    model = Alumno
    template_name = "alumno_list.html"

class AlumnoCreate (CreateView):
    model = Alumno
    form_class = AlumnoForm
    template_name = "alumno_create.html"
    success_url = reverse_lazy ('persona:alumno_list')

class AlumnoDetail (DetailView):
    model = Alumno
    template_name = "alumno_detail.html"

class AlumnoUpdate (UpdateView):
    model = Alumno
    form_class = AlumnoForm
    template_name = "alumno_create.html"
    success_url = reverse_lazy('persona:alumno_list')

class AlumnoDelete (DeleteView):
    model = Alumno
    template_name = "alumno_confirm_delete.html"
    success_url = reverse_lazy('persona:alumno_list')
    confirm_message = '¿Está seguro de que desea eliminar al alumno?'
