from django.urls import path
from . import views

app_name = 'evaluacion'

ulrpatterns = [
    #EvaluacionPTF views
    path ('evaluacion_ptf/<int:pk>', views.evaluacion_ptf_list, name='evaluacion_ptf_list'),
]