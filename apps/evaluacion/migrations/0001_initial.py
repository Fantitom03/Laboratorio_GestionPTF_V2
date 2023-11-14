# Generated by Django 4.2.7 on 2023-11-14 23:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('proyectotf', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='EvaluacionPTF',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('informe', models.FileField(blank=True, null=True, upload_to='')),
                ('fecha_evaluacion', models.DateField()),
                ('estado', models.CharField(choices=[('aprobado', 'Aprobado'), ('observado', 'Observado'), ('rechazado', 'Rechazado')], max_length=20)),
                ('observaciones', models.CharField(blank=True, max_length=500, null=True)),
                ('proyecto_TF', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proyectotf.proyecto_tf')),
            ],
        ),
        migrations.CreateModel(
            name='EvaluacionITF',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('informe', models.FileField(null=True, upload_to='')),
                ('fecha_evaluacion', models.DateField()),
                ('estado', models.CharField(choices=[('aprobado', 'Aprobado'), ('observado', 'Observado'), ('rechazado', 'Rechazado')], max_length=20)),
                ('observaciones', models.CharField(max_length=500, null=True)),
                ('informe_TF', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proyectotf.informe_tf')),
            ],
        ),
        migrations.CreateModel(
            name='Defensa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('informe', models.FileField(null=True, upload_to='')),
                ('fecha_evaluacion', models.DateField()),
                ('estado', models.CharField(choices=[('aprobado', 'Aprobado'), ('rechazado', 'Rechazado')], max_length=20)),
                ('informe_TF', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proyectotf.informe_tf')),
            ],
        ),
    ]