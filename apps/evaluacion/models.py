from django.db import models
from apps.proyectotf.models import Proyecto_TF, Informe_TF

class EvaluacionPTF(models.Model):

    estado_op = (
        ('aprobado', 'Aprobado'),
        ('observado', 'Observado'),
        ('rechazado', 'Rechazado')
    )

    proyecto_TF = models.ForeignKey(Proyecto_TF, on_delete = models.CASCADE)
    informe = models.FileField(blank=True, null=True)
    fecha_evaluacion = models.DateField()
    estado = models.CharField(max_length=20, choices=estado_op)
    observaciones = models.CharField(max_length=500, blank=True, null=True)


class EvaluacionITF(models.Model):
    estado_op = (
        ('aprobado', 'Aprobado'),
        ('observado', 'Observado'),
        ('rechazado', 'Rechazado')
    )

    informe_TF = models.ForeignKey(Informe_TF, on_delete=models.CASCADE)
    informe = models.FileField(null=True)
    fecha_evaluacion = models.DateField()
    estado = models.CharField(max_length=20, choices=estado_op)
    observaciones = models.CharField(max_length=500, null=True)

class Defensa(models.Model):

    estado_op = (
        ('aprobado', 'Aprobado'),
        ('rechazado', 'Rechazado')
    )

    informe_TF = models.ForeignKey(Informe_TF, on_delete=models.CASCADE)
    informe = models.FileField(null=True)
    fecha_evaluacion = models.DateField()
    estado = models.CharField(max_length=20, choices=estado_op)
