from django.db import models

class Persona (models.Model):
    dni = models.CharField(max_length=8, unique=True, blank=False)
    nombre = models.CharField(max_length=100, blank=False)
    apellido = models.CharField(max_length=100, blank=False)

    @property
    def nombre_completo(self):
        return f"{self.nombre} {self.apellido}"
        # O usando str.format():
        # return "{} {}".format(self.nombre, self.apellido)

    def __str__(self):
        return '{}'.format(self.nombre_completo)

class Docente (Persona):
    cuil = models.CharField(max_length=11, unique=True, blank=False)

class Alumno (Persona):
    matricula = models.CharField(max_length=5, unique=True, blank=False)
    correo_electronico = models.EmailField(max_length=254, blank=False)

class Asesor (Persona):
    curriculum = models.FileField(null=True)



