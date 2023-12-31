from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect, get_object_or_404, reverse
from .forms import EvaluacionPTF_Form, EvaluacionITF_Form, Defensa_Form
from apps.proyectotf.forms import Proyecto_TF_Form, Proyecto_TF_AlumnoForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .models import EvaluacionITF, EvaluacionPTF, Defensa, Proyecto_TF, Informe_TF
from .forms import EvaluacionITF_Form, EvaluacionPTF_Form, Defensa_Form
from ..comision.models import Miembro_TE, TribunalEvaluador
from ..persona.models import Docente
from ..proyectotf.models import Proyecto_TF_Alumno


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
            form.save()
            estado_nuevo = form.cleaned_data["estado"]
            proyecto.estado = estado_nuevo
            proyecto.save()
            return redirect('evaluacion:evaluacion_ptf_list', pk=pk)
    else:
        form = EvaluacionPTF_Form()
    return render(request, 'evaluacion_ptf_create.html', {'form':form, 'proyecto':proyecto})


@login_required(login_url='usuarios:login')
@permission_required('evaluacion.change_evaluacionptf',
raise_exception=True)
def evaluacion_ptf_edit (request, pk):
    evaluacion = get_object_or_404(EvaluacionPTF, pk=pk)
    if request.method == 'POST':
        form = EvaluacionPTF_Form(request.POST, request.FILES, instance=evaluacion)
        if form.is_valid():
            evaluacion_editada = form.save()
            evaluacion = evaluacion_editada
            evaluacion.save()
            proyecto = get_object_or_404(Proyecto_TF, pk=evaluacion.proyecto_TF.pk)
            estado_nuevo = form.cleaned_data["estado"]
            proyecto.estado = estado_nuevo
            proyecto.save()
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



@login_required(login_url='usuarios:login')
@permission_required('proyectotf.view_proyectotf_te',
raise_exception=True)
def evaluacionptf_tribunal(request):
    docente = get_object_or_404(Docente, cuil=request.user.username)
    miembrote = get_object_or_404(Miembro_TE, docente=docente)
    tribunal = get_object_or_404(TribunalEvaluador, miembros=miembrote)
    proyectotfs = Proyecto_TF_Alumno.objects.filter(proyecto_tf__te_asignado=tribunal)
    return render(request, 'seleccionar_ptf.html', {'proyectotfs': proyectotfs})

@login_required(login_url='usuarios:login')
@permission_required('proyectotf.view_proyectotf_te',
raise_exception=True)
def evaluacionitf_tribunal(request):
    docente = get_object_or_404(Docente, cuil=request.user.username)
    miembrote = get_object_or_404(Miembro_TE, docente=docente)
    tribunal = get_object_or_404(TribunalEvaluador, miembros=miembrote)
    informetfs = Informe_TF.objects.filter(proyecto_tf__te_asignado=tribunal)

    return render(request, 'seleccionar_itf.html', {'informetfs': informetfs})









@login_required(login_url='usuarios:login')
@permission_required('evaluacion.view_evaluacionitf',
raise_exception=True)
def evaluacion_itf_list (request, pk):
    informe = get_object_or_404(Informe_TF, pk=pk)
    evaluaciones = EvaluacionITF.objects.filter(informe_TF=informe)
    return render(request, 'evaluacion_itf_list.html', {'evaluaciones':evaluaciones, 'informe':informe})


@login_required(login_url='usuarios:login')
@permission_required('evaluacion.add_evaluacionitf',
raise_exception=True)
def evaluacion_itf_create (request, pk):
    informe = get_object_or_404(Informe_TF, pk=pk)

    if request.method == 'POST':
        form = EvaluacionITF_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            estado_nuevo = form.cleaned_data["estado"]
            informe.estado = estado_nuevo
            informe.save()
            return redirect('evaluacion:evaluacion_itf_list', pk=pk)
    else:
        form = EvaluacionITF_Form()
    return render(request, 'evaluacion_itf_create.html', {'form':form, 'informe':informe})


@login_required(login_url='usuarios:login')
@permission_required('evaluacion.change_evaluacionitf',
raise_exception=True)
def evaluacion_itf_edit (request, pk):
    evaluacion = get_object_or_404(EvaluacionITF, pk=pk)
    if request.method == 'POST':
        form = EvaluacionITF_Form(request.POST, request.FILES, instance=evaluacion)
        if form.is_valid():
            evaluacion_editada = form.save()
            evaluacion = evaluacion_editada
            evaluacion.save()
            informe = get_object_or_404(Informe_TF, pk=evaluacion.informe_TF.pk)
            estado_nuevo = form.cleaned_data["estado"]
            informe.estado = estado_nuevo
            informe.save()
            return redirect('evaluacion:evaluacion_itf_list', evaluacion.informe_TF.id)
    else:
        form = EvaluacionITF_Form(instance=evaluacion)
    return render(request, 'evaluacion_itf_edit.html', {'form':form, 'evaluacion':evaluacion})



@login_required(login_url='usuarios:login')
@permission_required('evaluacion.delete_evaluacionpitf',
raise_exception=True)
def evaluacion_itf_delete(request, pk):
    evaluacion = get_object_or_404(EvaluacionITF, pk=pk)
    if request.method == 'POST':
        evaluacion.delete()
        return redirect('evaluacion:evaluacion_itf_list', evaluacion.informe_TF.id)
    return render(request, 'evaluacion_itf_confirm_delete.html', {'evaluacion': evaluacion})
