from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .models import EvaluacionITF, EvaluacionPTF, Defensa, Proyecto_TF, Informe_TF
from .forms import EvaluacionITF_Form, EvaluacionPTF_Form, Defensa_Form

def evaluacion_ptf_list (request, pk):
    ptf = Proyecto_TF.objects.filter(pk=pk)
    evaluaciones = EvaluacionPTF.objects.filter(proyecto_tf=ptf)
    return render(request, 'evaluacion_ptf_list.html', {'evaluaciones':evaluaciones, 'proyecto':ptf})



