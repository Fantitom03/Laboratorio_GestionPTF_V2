from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .models import Alumno, Docente, Asesor
from .forms import AlumnoForm, AsesorForm, DocenteForm


#-----------
#ALUMNOS
#-----------

@login_required(login_url='usuarios:login')
@permission_required('persona.view_alumno',
raise_exception=True)
def alumno_list (request):
    alumnos = Alumno.objects.all().order_by('dni')
    return render(request, 'alumno_list.html', {'alumnos':alumnos})







@login_required(login_url='usuarios:login')
@permission_required('persona.view_alumno',
raise_exception=True)
def alumno_detail (request, pk):
    alumno = get_object_or_404(Alumno, pk=pk)
    return render(request, 'alumno_detail.html', {'alumno': alumno})


@login_required(login_url='usuarios:login')
@permission_required('persona.add_alumno',
raise_exception=True)
def alumno_create (request):
    if request.method == 'POST':
        form = AlumnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('persona:alumno_list')
    else:
        form = AlumnoForm()
    return render(request, 'alumno_create.html', {'form':form})


@login_required(login_url='usuarios:login')
@permission_required('persona.change_alumno',
raise_exception=True)
def alumno_edit (request, pk):
    alumno = get_object_or_404(Alumno, pk=pk)
    if request.method == 'POST':
        form = AlumnoForm(request.POST, instance=alumno)
        if form.is_valid():
            form.save()
            return redirect('persona:alumno_detail', pk=alumno.pk)
        else:
            messages.error(request, 'Por favor, corrija los errores en el formulario.')
    else:
        form = AlumnoForm(instance=alumno)

    return render(request, 'alumno_edit.html', {'form':form, 'alumno':alumno})


@login_required(login_url='usuarios:login')
@permission_required('persona.delete_alumno',
raise_exception=True)
def alumno_delete (request, pk):
    alumno = get_object_or_404(Alumno, pk=pk)
    if request.method == 'POST':
        alumno.delete()
        return redirect('persona:alumno_list')
    return render(request, 'alumno_confirm_delete.html', {'alumno':alumno})


#-----------
#ASESORES
#-----------

@login_required(login_url='usuarios:login')
@permission_required('persona.view_asesor',
raise_exception=True)
def asesor_list(request):
    asesores = Asesor.objects.all()
    return render(request, 'asesor_list.html', {'asesores': asesores})


@login_required(login_url='usuarios:login')
@permission_required('persona.view_alumno',
raise_exception=True)
def asesor_detail(request, pk):
    asesor = get_object_or_404(Asesor, pk=pk)
    return render(request, 'asesor_detail.html', {'asesor': asesor})


@login_required(login_url='usuarios:login')
@permission_required('persona.add_asesor',
raise_exception=True)
def asesor_create(request):
    if request.method == 'POST':
        form = AsesorForm(request.POST, request.FILES)
        if form.is_valid():
            nuevo_asesor = form.save(commit=True)
            messages.success(request, 'Se ha agregado correctamente el Asesor {}'.format(nuevo_asesor))
            return redirect(reverse('persona:asesor_list'))
    else:
        form = AsesorForm()
    return render(request, 'asesor_create.html', {'form': form})


@login_required(login_url='usuarios:login')
@permission_required('persona.change_asesor',
raise_exception=True)
def asesor_edit(request, pk):
    asesor = get_object_or_404(Asesor, pk=pk)
    if request.method == 'POST':
        form = AsesorForm(request.POST, request.FILES, instance=asesor)
        if form.is_valid():
            asesor_editado = form.save(commit=True)
            asesor = asesor_editado
            asesor.save()
            messages.success(request, 'Se ha actualizado correctamente el Asesor')
            return redirect('persona:asesor_detail', pk=asesor.pk)
        else:
            messages.error(request, 'Por favor, corrija los errores en el formulario.')
    else:
        form = AsesorForm(instance=asesor)
    return render(request, 'asesor_edit.html', {'form': form, 'asesor': asesor})



@login_required(login_url='usuarios:login')
@permission_required('persona.delete_asesor',
raise_exception=True)
def asesor_delete(request, pk):
    asesor = get_object_or_404(Asesor, pk=pk)
    if request.method == 'POST':
        asesor.delete()
        return redirect('persona:asesor_list')
    return render(request, 'asesor_confirm_delete.html', {'asesor':asesor})

#-----------
#DOCENTES
#-----------


@login_required(login_url='usuarios:login')
@permission_required('persona.view_docente',
raise_exception=True)
def docente_list (request):
    docentes = Docente.objects.all()
    return render(request, 'docente_list.html', {'docentes': docentes})


@login_required(login_url='usuarios:login')
@permission_required('persona.view_docente',
raise_exception=True)
def docente_detail (request, pk):
    docente = get_object_or_404(Docente,pk=pk)
    return render(request, 'docente_detail.html', {'docente':docente})


@login_required(login_url='usuarios:login')
@permission_required('persona.add_docente',
raise_exception=True)
def docente_create (request):
    if request.method == 'POST':
        form = DocenteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('persona:docente_list'))
    else:
        form = DocenteForm()
    return render(request, 'docente_create.html', {'form':form})


@login_required(login_url='usuarios:login')
@permission_required('persona.change_docente',
raise_exception=True)
def docente_edit(request, pk):
    docente = get_object_or_404(Docente, pk=pk)
    if request.method == 'POST':
        form = DocenteForm(request.POST, instance=docente)
        if form.is_valid():
            docente_editado = form.save(commit=True)
            docente = docente_editado
            docente.save()
            return redirect('persona:docente_detail', pk=docente.pk)
        else:
            messages.error(request, 'Por favor, corrija los errores en el formulario.')
    else:
        form = DocenteForm(instance=docente)
    return render(request, 'docente_edit.html', {'form': form, 'docente': docente})


@login_required(login_url='usuarios:login')
@permission_required('persona.delete_docente',
raise_exception=True)
def docente_delete(request, pk):
    docente = get_object_or_404(Docente, pk=pk)
    if request.method == 'POST':
        docente.delete()
        return redirect('persona:docente_list')
    return render(request, 'docente_confirm_delete.html', {'docente':docente})

