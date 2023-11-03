from django.db import models
from apps.persona.models import Docente
from django.core.exceptions import ValidationError
from datetime import datetime

class Miembro_CSTF (models.Model):
    docente = models.ForeignKey(Docente, on_delete=models.CASCADE)
    resolucion_asignacion = models.IntegerField(unique=True)
    fecha_alta = models.DateField()


class Miembro_TE (models.Model):
    docente = models.ForeignKey(Docente, on_delete=models.CASCADE)
    rol_op = (
        ('presidente', 'Presidente'),
        ('vocal_titular', 'Vocal Titular'),
        ('vocal_suplente', 'Vocal Suplente')
    )
    rol = models.CharField(max_length=30, choices=rol_op)
    fecha_alta = models.DateField()


class TribunalEvaluador (models.Model):
    numero_disposicion = models.IntegerField()
    miembros = models.ManyToManyField(Miembro_TE)
    fecha_disposicion = models.DateField()
    archivo_disposicion = models.FileField(null=True)
