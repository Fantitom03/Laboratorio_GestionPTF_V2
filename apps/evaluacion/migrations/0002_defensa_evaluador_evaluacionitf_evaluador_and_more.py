# Generated by Django 4.2.7 on 2023-11-17 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluacion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='defensa',
            name='evaluador',
            field=models.CharField(choices=[('comision', 'Comision de Seguimiento de Trabajo Final'), ('tribunal', 'Tribunal Evaluador')], default='tribunal', max_length=50),
        ),
        migrations.AddField(
            model_name='evaluacionitf',
            name='evaluador',
            field=models.CharField(choices=[('comision', 'Comision de Seguimiento de Trabajo Final'), ('tribunal', 'Tribunal Evaluador')], default='tribunal', max_length=50),
        ),
        migrations.AddField(
            model_name='evaluacionptf',
            name='evaluador',
            field=models.CharField(choices=[('comision', 'Comision de Seguimiento de Trabajo Final'), ('tribunal', 'Tribunal Evaluador')], default='tribunal', max_length=50),
        ),
    ]