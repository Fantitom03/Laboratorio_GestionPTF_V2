from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect, get_object_or_404, reverse
from .forms import EvaluacionPTF_Form, EvaluacionITF_Form, Defensa_Form
from apps.proyectotf.forms import Proyecto_TF_Form
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .models import EvaluacionITF, EvaluacionPTF, Defensa, Proyecto_TF, Informe_TF
from .forms import EvaluacionITF_Form, EvaluacionPTF_Form, Defensa_Form


@login_required(login_url='usuarios:login')
@permission_required('evaluacion.view_evaluacionptf',
raise_exception=True)
def evaluacion_ptf_list (request, pk):
    proyecto = get_object_or_404(Proyecto_TF, pk=pk)
    evaluaciones = EvaluacionPTF.objects.filter(proyecto_TF=proyecto)
    return render(request, 'evaluacion_ptf_list.html', {'evaluaciones':evaluaciones, 'proyecto':proyecto})

@login_required(login_url='usuarios:login')
@permission_required('evaluacion.add_evaluacionptf',
raise_exception=True)
def evaluacion_ptf_create (request, pk):
    proyecto = get_object_or_404(Proyecto_TF, pk=pk)
    if request.method == 'POST':
        form = EvaluacionPTF_Form(request.POST, request.FILES)
        if form.is_valid():
            print('Entra por el valid')
            form.save()

            return redirect('evaluacion:evaluacion_ptf_list', pk=pk)
    else:
        print('Es un GET WTF')
        form = EvaluacionPTF_Form()
    return render(request, 'evaluacion_ptf_create.html', {'form':form, 'proyecto':proyecto})


@login_required(login_url='usuarios:login')
@permission_required('evaluacion.change_evaluacionptf',
raise_exception=True)
def evaluacion_ptf_edit (request, pk):
    evaluacion = get_object_or_404(EvaluacionPTF, pk=pk)
    if request.method == 'POST':
        form = EvaluacionPTF_Form(request.POST, request.FILES)
        if form.is_valid():
            evaluacion_editada = form.save(commit=False)
            evaluacion = evaluacion_editada
            evaluacion.save()
            return redirect('evaluacion:evaluacion_ptf_list', evaluacion.proyecto_TF.id)
    else:
        form = EvaluacionPTF_Form(instance=evaluacion)
    return render(request, 'evaluacion_ptf_edit.html', {'form':form, 'evaluacion':evaluacion})



@login_required(login_url='usuarios:login')
@permission_required('evaluacion.delete_evaluacionptf',
raise_exception=True)
def evaluacion_ptf_delete (request, pk):
    evaluacion = get_object_or_404(EvaluacionPTF, pk=pk)
    if request.method == 'POST':
        evaluacion.delete()
        return redirect('evaluacion:evaluacion_ptf_list', evaluacion.proyecto_TF.id)
    return render(request, 'evaluacion_ptf_confirm_delete.html', {'evaluacion': evaluacion})
