# Generated by Django 4.2.7 on 2023-11-14 23:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dni', models.CharField(max_length=8, unique=True)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('persona_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='persona.persona')),
                ('matricula', models.CharField(max_length=5, unique=True)),
                ('correo_electronico', models.EmailField(max_length=254)),
            ],
            bases=('persona.persona',),
        ),
        migrations.CreateModel(
            name='Asesor',
            fields=[
                ('persona_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='persona.persona')),
                ('curriculum', models.FileField(null=True, upload_to='')),
            ],
            bases=('persona.persona',),
        ),
        migrations.CreateModel(
            name='Docente',
            fields=[
                ('persona_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='persona.persona')),
                ('cuil', models.CharField(max_length=11, unique=True)),
            ],
            bases=('persona.persona',),
        ),
    ]