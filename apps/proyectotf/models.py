from django.db import models
from apps.persona.models import Docente, Alumno, Asesor
from apps.comision.models import TribunalEvaluador, Miembro_CSTF


class Proyecto_TF(models.Model):
    estado_op = (
        ('aprobado', 'Aprobado'),
        ('observado', 'Observado'),
        ('rechazado', 'Rechazado')
    )

    fecha_presentacion = models.DateField()
    director = models.OneToOneField(Docente, related_name='director_proyecto', on_delete=models.CASCADE)
    co_director = models.OneToOneField(Docente, related_name='codirector_proyecto', on_delete=models.CASCADE)
    asesor = models.OneToOneField(Asesor, related_name='asesor_proyecto', null=True, blank=True,
                                  on_delete=models.CASCADE)
    titulo_ptf = models.CharField(max_length=200)
    descripcion = models.TextField()
    archivos_adjuntos = models.FileField(null=True)
    certificado_analitico = models.FileField(null=True)
    nota_aceptacion_director = models.FileField(null=True)
    estado = models.CharField(max_length=20, choices=estado_op)
    observaciones = models.CharField(max_length=500, null=True)
    cstf = models.ForeignKey(Miembro_CSTF, on_delete=models.CASCADE)
    te_asignado = models.ForeignKey(TribunalEvaluador, on_delete=models.CASCADE)



class Proyecto_TF_Alumno(models.Model):
    proyecto_tf = models.ForeignKey(Proyecto_TF, related_name='alumnos', on_delete=models.CASCADE, null=True,
                                    blank=True)
    alumno = models.ForeignKey('persona.Alumno', related_name='proyectos_tf', on_delete=models.CASCADE)


class Informe_TF(models.Model):
    estado_op = (
        ('aprobado', 'Aprobado'),
        ('observado', 'Observado'),
        ('rechazado', 'Rechazado')
    )

    alumno = models.ForeignKey('persona.Alumno', related_name='informe_tf', on_delete=models.CASCADE)
    archivo_itf = models.FileField(upload_to='archivos_itf/', null=True)
    proyecto_tf = models.ForeignKey(Proyecto_TF, related_name='informes_tf', on_delete=models.CASCADE)
    estado = models.CharField(max_length=20, choices=estado_op)
    observaciones = models.CharField(max_length=500, null=True)



"""
# Obtener todos los alumnos de un proyecto específico
proyecto = Proyecto_TF.objects.get(id=1)  # Reemplaza 1 con el ID del proyecto que deseas consultar
alumnos_del_proyecto = proyecto.alumnos.all()

# Iterar sobre los alumnos del proyecto
for alumno in alumnos_del_proyecto:
    print(alumno.nombre_completo)
"""