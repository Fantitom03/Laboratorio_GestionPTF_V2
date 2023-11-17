from django.urls import path
from . import views

app_name = 'evaluacion'

urlpatterns = [
    #EvaluacionPTF views
    path('evaluacion_ptf/<int:pk>', views.evaluacion_ptf_list, name='evaluacion_ptf_list'),
    path('evaluacion_ptf/<int:pk>/nuevo/', views.evaluacion_ptf_create, name='evaluacion_ptf_create'),
    path('evaluacion_ptf/editar/<int:pk>', views.evaluacion_ptf_edit, name='evaluacion_ptf_edit'),
    path('evaluacion_ptf/delete/<int:pk>', views.evaluacion_ptf_delete, name='evaluacion_ptf_delete'),
]