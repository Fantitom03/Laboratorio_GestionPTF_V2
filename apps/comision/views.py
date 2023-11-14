from django.forms import modelformset_factory
from django.shortcuts import render, redirect, get_object_or_404, redirect
from django.urls import reverse
from django.contrib import messages
from .forms import Miembro_CSTF_Form, Miembro_TE_Form, TribunalEvaluadorForm
from .models import Miembro_CSTF, Miembro_TE, TribunalEvaluador

def miembrocstf_list(request):
    cstf = Miembro_CSTF.objects.all()
    return render(request, 'cstf_list.html', {'cstf': cstf})



# Vista para mostrar detalles de un miembrocstf específico
def miembrocstf_detail(request, pk):
    miembrocstf = get_object_or_404(Miembro_CSTF, pk=pk)
    return render(request, 'cstf_detail.html', {'miembrocstf': miembrocstf})


# Vista para crear un nuevo miembrocstf
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

def miembro_te_create(request, pk):
    tribunal = TribunalEvaluador.objects.filter(pk=pk)
    if request.method == 'POST':
        form = Miembro_TE_Form(request.POST, pk=pk)
        if form.is_valid():
            nuevo_miembro_te = form.save(commit=False)
            tribunal.miembros.add(nuevo_miembro_te)
            tribunal.save()
            messages.success(request, 'Se ha agregado correctamente el miembro del Tribunal Evaluador {}'.format(nuevo_miembro_te))
            return redirect('comision:tribunal_detail', pk=pk)
    else:
        form = Miembro_TE_Form()
    return render(request, 'miembrote_create.html', {'form': form, 'tribunal': tribunal})

def miembro_te_list(request):
    total_miembros = Miembro_TE.objects.count()  # Contar el número de miembros del tribunal evaluador
    miembros_te = Miembro_TE.objects.all()
    return render(request, 'miembrote_list.html', {'miembros_te': miembros_te, 'total_miembros': total_miembros})

def miembro_te_detail(request, pk):
    miembro_te = get_object_or_404(Miembro_TE, pk=pk)
    tribunales_pertenecientes = miembro_te.tribunalevaluador_set.all()  # Esto te dará todos los tribunales a los que pertenece este miembro
    return render(request, 'miembrote_detail.html', {'miembro_te': miembro_te, 'tribunales': tribunales_pertenecientes})

# Vista para actualizar un miembro de TribunalEvaluador existente
def miembro_te_edit(request, pk, tribunal):
    miembrote = get_object_or_404(Miembro_TE, pk=pk)
    if request.method == 'POST':
        form = Miembro_TE_Form(request.POST, instance=miembrote)
        if form.is_valid():
            form.save()
            messages.success(request, 'Se ha actualizado correctamente el miembro del tribunal evaluador')
            return redirect('comision:tribunal_detail', pk=miembrote.pk)
        else:
            messages.error(request, 'Por favor, corrija los errores en el formulario.')
    else:
        form = Miembro_TE_Form(instance=miembrote)
    return redirect('comision:tribunal_detail', tpk=tribunal)

# Vista para eliminar un miembro de TribunalEvaluador existente
def miembro_te_delete(request, pk, tribunal):
    if request.method == 'POST':
        if 'id_miembrote' in request.POST:
            miembrote = get_object_or_404(Miembro_TE, pk=pk)
            miembrote.delete()
            messages.success(request, 'Se ha eliminado exitosamente el miembro del tribunal evaluador')
        else:
            messages.error(request, 'Debe indicar qué miembro del tribunal evaluador desea eliminar')
    return redirect('comision:tribunal_detail', tpk=tribunal)


#
#
#
#
#



def tribunal_create(request):
    if request.method == 'POST':
        form = TribunalEvaluadorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=True)

            return redirect(reverse('comision:tribunal_list'))
    else:
        form = TribunalEvaluadorForm()
    return render(request, 'tribunal_create.html', {'form': form})




def tribunal_list(request):
    tribunales = TribunalEvaluador.objects.all()
    return render(request, 'tribunal_list.html', {'tribunales': tribunales})


def tribunal_detail(request, pk):
    miembros_te = Miembro_TE.objects.filter(pk=tribunal.pk)
    tribunal = get_object_or_404(TribunalEvaluador, pk=pk)
    return render(request, 'tribunal_detail.html', {'tribunal': tribunal, 'miembros_te': miembros_te})




def tribunal_edit(request, pk):
    tribunal = get_object_or_404(TribunalEvaluador, pk=pk)
    if request.method == 'POST':
        tribunal_form = TribunalEvaluadorForm(request.POST, request.FILES, instance=tribunal)
        miembro_formset = Miembro_TE_Form(request.POST, prefix='miembro', queryset=tribunal.miembros.all())

        if tribunal_form.is_valid() and miembro_formset.is_valid():
            tribunal = tribunal_form.save(commit=False)
            tribunal.save()
            miembro_formset.save(commit=False)
            for form in miembro_formset.forms:
                if form.cleaned_data.get('docente') and form.cleaned_data.get('rol') and form.cleaned_data.get(
                        'fecha_alta'):
                    miembro = form.save(commit=False)
                    miembro.tribunal = tribunal
                    miembro.save()
            messages.success(request, 'Tribunal evaluador actualizado correctamente.')
            return redirect('comision:tribunal_detail', pk=tribunal.pk)
    else:
        tribunal_form = TribunalEvaluadorForm(instance=tribunal)
        miembro_formset = Miembro_TE_Form(prefix='miembro', queryset=tribunal.miembros.all())
    return render(request, 'tribunal_edit.html',
                  {'tribunal_form': tribunal_form, 'miembro_formset': miembro_formset, 'tribunal': tribunal})


def tribunal_delete(request, pk):
    tribunal = get_object_or_404(TribunalEvaluador, pk=pk)
    if request.method == 'POST':
        tribunal.delete()
        messages.success(request, 'Tribunal evaluador eliminado correctamente.')
        return redirect('comision:tribunal_list')
    return render(request, 'tribunal_confirm_delete.html', {'tribunal': tribunal})