
from django.contrib.auth.decorators import login_required, permission_required
from django.db import connection

from django.forms import modelformset_factory
from django.shortcuts import render, redirect, get_object_or_404, redirect
from django.urls import reverse
from django.contrib import messages
from .forms import Miembro_CSTF_Form, Miembro_TE_Form, TribunalEvaluadorForm
from .models import Miembro_CSTF, Miembro_TE, TribunalEvaluador


@login_required(login_url='usuarios:login')
@permission_required('comision.view_miembro_cstf',
raise_exception=True)

def miembrocstf_list(request):
    cstf = Miembro_CSTF.objects.all()
    return render(request, 'cstf_list.html', {'cstf': cstf})



# Vista para mostrar detalles de un miembrocstf específico
@login_required(login_url='usuarios:login')
@permission_required('comision.view_miembro_cstf',
raise_exception=True)
def miembrocstf_detail(request, pk):
    miembrocstf = get_object_or_404(Miembro_CSTF, pk=pk)
    return render(request, 'cstf_detail.html', {'miembrocstf': miembrocstf})


# Vista para crear un nuevo miembrocstf
@login_required(login_url='usuarios:login')
@permission_required('comision.add_miembro_cstf',
raise_exception=True)
def miembrocstf_create(request):
    if request.method == 'POST':
        form = Miembro_CSTF_Form(request.POST)
        if form.is_valid():
            nuevo_miembrocstf = form.save(commit=False)
            nuevo_miembrocstf.clean()  # Llama al método clean del modelo
            nuevo_miembrocstf.save()
            messages.success(request, 'Se ha agregado correctamente el miembro de la cstf {}'.format(nuevo_miembrocstf))
            return redirect(reverse('comision:cstf_list'))
    else:
        form = Miembro_CSTF_Form()
    return render(request, 'cstf_create.html', {'form': form})


# Vista para actualizar un miembrocstf existente
@login_required(login_url='usuarios:login')
@permission_required('comision.change_miembro_cstf',
raise_exception=True)
def miembrocstf_edit(request, pk):
    miembrocstf = get_object_or_404(Miembro_CSTF, pk=pk)
    if request.method == 'POST':
        form = Miembro_CSTF_Form(request.POST, instance=miembrocstf)
        if form.is_valid():
            miembrocstf_editado = form.save(commit=True)
            miembrocstf = miembrocstf_editado
            miembrocstf.save()
            messages.success(request, 'Se ha actualizado correctamente el miembrocstf')
            return redirect('comision:cstf_detail', pk=miembrocstf.pk)
        else:
            messages.error(request, 'Por favor, corrija los errores en el formulario.')
    else:
        form = Miembro_CSTF_Form(instance=miembrocstf)
    return render(request, 'cstf_edit.html', {'form': form, 'miembrocstf': miembrocstf})


# Vista para eliminar un docente existente
@login_required(login_url='usuarios:login')
@permission_required('comision.delete_miembro_cstf',
raise_exception=True)
def miembrocstf_delete(request, pk):
    if request.method == 'POST':
        if 'id_miembrocstf' in request.POST:
            miembrocstf = get_object_or_404(Miembro_CSTF, pk=pk)
            nombre_persona = miembrocstf.docente.nombre
            miembrocstf.delete()
            messages.success(request, 'Se ha eliminado exitosamente el miembrocstf {}'.format(nombre_persona))
        else:
            messages.error(request, 'Debe indicar qué miembrocstf desea eliminar')
    return redirect(reverse('comision:cstf_list'))

#
#
#
#
#MIEMBROS TRIBUNAL EVALUADOR
#
@login_required(login_url='usuarios:login')
@permission_required('comision.add_miembro_te',
raise_exception=True)
def miembro_te_create(request, pk):
    tribunal = TribunalEvaluador.objects.get(pk=pk)

    if request.method == 'POST':
        form = Miembro_TE_Form(request.POST)
        if form.is_valid():
            print(form.cleaned_data['docente'])

            nuevo_miembro_te = form.save()

            tribunal.miembros.add(nuevo_miembro_te)
            tribunal.save()
            messages.success(request, 'Se ha agregado correctamente el miembro del Tribunal Evaluador {}'.format(nuevo_miembro_te))
            return redirect('comision:tribunal_detail', pk=tribunal.pk)
    else:
        form = Miembro_TE_Form()
    return render(request, 'miembrote_create.html', {'form': form, 'tribunal': tribunal})

@login_required(login_url='usuarios:login')
@permission_required('comision.change_miembro_te',
raise_exception=True)
def miembro_te_edit(request, pk):
    miembrote = get_object_or_404(Miembro_TE, pk=pk)

    if request.method == 'POST':
        form = Miembro_TE_Form(request.POST, request.FILES, instance=miembrote)
        if form.is_valid():
            miembrote_editado = form.save()
            miembrote = miembrote_editado
            miembrote.save()
            return redirect('comision:tribunal_list')
        else:
            messages.error(request, 'Por favor, corrija los errores en el formulario.')
    else:
        form = Miembro_TE_Form(instance=miembrote)
    return render(request, 'miembrote_edit.html', {'miembrote': miembrote, 'form': form })




@login_required(login_url='usuarios:login')
@permission_required('comision.delete_miembro_te',
raise_exception=True)
def miembro_te_delete(request, pk):
    miembrote = get_object_or_404(Miembro_TE, pk=pk)
    if request.method == 'POST':
        print('SISELIMINO')
        miembrote.delete()
        messages.success(request, 'Se ha eliminado exitosamente el miembro del tribunal evaluador')
        return redirect('comision:tribunal_list')
    return render(request, 'miembro_confirm_delete.html', {'miembrote': miembrote})



#
#
#
#
#


@login_required(login_url='usuarios:login')
@permission_required('comision.add_tribunalevaluador',
raise_exception=True)
def tribunal_create(request):
    if request.method == 'POST':
        form = TribunalEvaluadorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=True)

            return redirect(reverse('comision:tribunal_list'))
    else:
        form = TribunalEvaluadorForm()
    return render(request, 'tribunal_create.html', {'form': form})



@login_required(login_url='usuarios:login')
@permission_required('comision.view_tribunalevaluador',
raise_exception=True)

def tribunal_list(request):
    tribunales = TribunalEvaluador.objects.all()
    return render(request, 'tribunal_list.html', {'tribunales': tribunales})

@login_required(login_url='usuarios:login')
@permission_required('comision.view_tribunalevaluador',
raise_exception=True)
def tribunal_detail(request, pk):
    tribunal = get_object_or_404(TribunalEvaluador, pk=pk)
    miembros_te = tribunal.miembros.all()
    return render(request, 'tribunal_detail.html', {'tribunal': tribunal, 'miembros_te': miembros_te})

@login_required(login_url='usuarios:login')
@permission_required('comision.change_tribunalevaluador',
raise_exception=True)
def tribunal_edit(request, pk):
    tribunal = get_object_or_404(TribunalEvaluador, pk=pk)
    if request.method == 'POST':
        form = TribunalEvaluadorForm(request.POST, request.FILES, instance=tribunal)
        if form.is_valid():
            tribunal_editado = form.save()
            tribunal = tribunal_editado
            tribunal.save()
            return redirect('comision:tribunal_detail', pk=tribunal.pk)
    else:
        form = TribunalEvaluadorForm(instance=tribunal)
    return render(request, 'tribunal_edit.html', {'form': form, 'tribunal': tribunal})

@login_required(login_url='usuarios:login')
@permission_required('comision.delete_tribunalevaluador',
raise_exception=True)
def tribunal_delete(request, pk):
    tribunal = get_object_or_404(TribunalEvaluador, pk=pk)
    if request.method == 'POST':
        tribunal.delete()
        messages.success(request, 'Tribunal evaluador eliminado correctamente.')
        return redirect('comision:tribunal_list')
    return render(request, 'tribunal_confirm_delete.html', {'tribunal': tribunal})