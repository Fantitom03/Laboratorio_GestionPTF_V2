from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib import messages
from .forms import Proyecto_TF_AlumnoForm, Proyecto_TF_Form, Informe_TF_Form
from .models import Proyecto_TF_Alumno, Informe_TF
from django.contrib.auth import authenticate, login, logout


def proyectotf_list(request):
    proyectotfs = Proyecto_TF_Alumno.objects.all()
    for proyecto in proyectotfs:
        print(proyecto.alumno)

    return render(request, 'proyectotf_list.html', {'proyectotfs': proyectotfs})



# Vista para mostrar detalles de un proyectotf específico
def proyectotf_detail(request, pk):
    proyectotf = get_object_or_404(Proyecto_TF_Alumno, pk=pk)
    return render(request, 'proyectotf_detail.html', {'proyectotf': proyectotf})


def proyectotf_create(request):
    if request.method == 'POST':
        form = Proyecto_TF_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('proyectotf:proyectotf_miembros_create')
    else:
        form = Proyecto_TF_Form()
    return render(request, 'proyectotf_create.html', {'form': form})

# Vista para crear un nuevo proyectotf
def proyectotf_miembros_create(request):
    if request.method == 'POST':
        form = Proyecto_TF_AlumnoForm(request.POST)
        if form.is_valid():
            nuevo_proyectotf_miembros = form.save(commit=True)
            messages.success(request, 'Se ha agregado correctamente el proyectotf {}'.format(nuevo_proyectotf_miembros))
            return redirect(reverse('proyectotf:proyectotf_list'))
    else:
        form = Proyecto_TF_AlumnoForm()
    return render(request, 'proyectotf_miembros_create.html', {'form': form})



# Vista para actualizar un proyectotf existente
def proyectotf_miembro_edit(request, pk):
    proyectotf = get_object_or_404(Proyecto_TF_Alumno, pk=pk)
    if request.method == 'POST':
        form = Proyecto_TF_AlumnoForm(request.POST, instance=proyectotf)
        if form.is_valid():
            proyectotf_editado = form.save(commit=True)
            proyectotf = proyectotf_editado
            proyectotf.save()
            messages.success(request, 'Se ha actualizado correctamente el Proyecto_TF')
            return redirect('proyectotf:proyectotf_detail', pk=proyectotf.pk)
        else:
            messages.error(request, 'Por favor, corrija los errores en el formulario.')
    else:
        form = Proyecto_TF_AlumnoForm(instance=proyectotf)
    return render(request, 'proyectotf_miembros_edit.html', {'form': form, 'proyectotf': proyectotf})

def proyectotf_edit(request, pk):
    proyectotf_relacion = get_object_or_404(Proyecto_TF_Alumno, pk=pk)
    proyectotf = proyectotf_relacion.proyecto_tf.id
    if request.method == 'POST':
        form = Proyecto_TF_Form(request.POST, instance=proyectotf)
        if form.is_valid():
            proyectotf_editado = form.save(commit=True)
            proyectotf = proyectotf_editado
            proyectotf.save()
            messages.success(request, 'Se ha actualizado correctamente el Proyecto_TF')
            return redirect('proyectotf:proyectotf_detail', pk=proyectotf_relacion.pk)
        else:
            messages.error(request, 'Por favor, corrija los errores en el formulario.')
    else:
        form = Proyecto_TF_AlumnoForm(instance=proyectotf_relacion)
    return render(request, 'proyectotf_edit.html', {'form': form, 'proyectotf_relacion': proyectotf_relacion})




# Vista para eliminar un proyectotf existente
def proyectotf_delete(request, pk):
    if request.method == 'POST':
        if 'id_proyectotf' in request.POST:
            proyectotf_id = request.POST['id_proyectotf']
            proyectotf = get_object_or_404(Proyecto_TF_Alumno, pk=proyectotf_id)
            nombre_proyectotf = proyectotf.proyecto_tf.titulo_ptf
            proyectotf.delete()
            messages.success(request, 'Se ha eliminado exitosamente el Proyecto_TF {}'.format(nombre_proyectotf))
        else:
            messages.error(request, 'Debe indicar qué Proyecto_TF desea eliminar')
    return redirect(reverse('proyectotf:proyectotf_list'))

#
#
#
#
#

def informetf_list(request):
    informetfs = Informe_TF.objects.all()
    return render(request, 'informetf_list.html', {'informetfs': informetfs})

def informetf_detail(request, pk):
    informetf = get_object_or_404(Informe_TF, pk=pk)
    return render(request, 'informetf_detail.html', {'informetf': informetf})


def informetf_create(request):
    if request.method == 'POST':
        form = Informe_TF_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('proyectotf:informetf_list')
    else:
        form = Informe_TF_Form()
    return render(request, 'informetf_create.html', {'form': form})




def informetf_edit(request, pk):
    informetf = get_object_or_404(Informe_TF, pk=pk)
    if request.method == 'POST':
        form = Informe_TF_Form(request.POST, instance=informetf)
        if form.is_valid():
            informetf_editado = form.save(commit=True)
            informetf = informetf_editado
            informetf.save()
            messages.success(request, 'Se ha actualizado correctamente el Proyecto_TF')
            return redirect('proyectotf:informetf_detail', pk=informetf.pk)
        else:
            messages.error(request, 'Por favor, corrija los errores en el formulario.')
    else:
        form = Informe_TF_Form(instance=informetf)
    return render(request, 'informetf_edit.html', {'form': form, 'informetf': informetf})


def informetf_delete(request, pk):
    informetf = get_object_or_404(Informe_TF, pk=pk)
    if request.method == 'POST':
        informetf.delete()
        messages.success(request, 'InformeTF eliminado correctamente.')
        return redirect('proyectotf:informetf_list')
    return render(request, 'informetf_confirm_delete.html', {'informetf': informetf})











































