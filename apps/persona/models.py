from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


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
    correo_electronico = models.EmailField(max_length=254, blank=False, null=True)
    crear_usuario = models.BooleanField(default=True)


@receiver(post_save, sender=Docente)
def crear_usuario_docente(sender, instance, created, **kwargs):
    # Verifica la condición crear_usuario
    if created:
        username = instance.cuil
        password = User.objects.make_random_password()
        user = User.objects.create_user(username=username, password=password)
        user.email = instance.correo_electronico
        user.save()

        # Envía el correo electrónico con las credenciales
        send_mail(
            'Datos del usuario',
            f'Nombre de usuario: {username}\nContraseña: {password}',
            'sistemadeseguimientoPTF@gmail.com',  # Reemplaza con tu dirección de correo
            [instance.correo_electronico],
            fail_silently=True,
        )

class Alumno (Persona):
    matricula = models.CharField(max_length=5, unique=True, blank=False)
    correo_electronico = models.EmailField(max_length=254, blank=False)
    crear_usuario = models.BooleanField(default=True)


@receiver(post_save, sender=Alumno)
def crear_usuario_alumno(sender, instance, created, **kwargs):
    # Verifica la condición crear_usuario
    if created:
        username = instance.dni
        password = User.objects.make_random_password()
        user = User.objects.create_user(username=username, password=password)
        user.email = instance.correo_electronico
        user.save()

        # Envía el correo electrónico con las credenciales
        send_mail(
            'Datos del usuario',
            f'Nombre de usuario: {username}\nContraseña: {password}',
            'sistemadeseguimientoPTF@gmail.com',  # Reemplaza con tu dirección de correo
            [instance.correo_electronico],
            fail_silently=True,
        )

class Asesor (Persona):
    curriculum = models.FileField(null=True)





