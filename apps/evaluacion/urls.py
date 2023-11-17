from django.urls import path
from . import views

app_name = 'evaluacion'

urlpatterns = [
    #EvaluacionPTF views
    path('evaluacion_ptf/<int:pk>', views.evaluacion_ptf_list, name='evaluacion_ptf_list'),
    path('evaluacion_ptf/<int:pk>/nuevo/', views.evaluacion_ptf_create, name='evaluacion_ptf_create'),
    path('evaluacion_ptf/editar/<int:pk>', views.evaluacion_ptf_edit, name='evaluacion_ptf_edit'),
    path('evaluacion_ptf/delete/<int:pk>', views.evaluacion_ptf_delete, name='evaluacion_ptf_delete'),

    #EvaluacionITF views
    path('evaluacion_itf/<int:pk>', views.evaluacion_itf_list, name='evaluacion_itf_list'),
    path('evaluacion_itf/<int:pk>/nuevo/', views.evaluacion_itf_create, name='evaluacion_itf_create'),
    path('evaluacion_itf/editar/<int:pk>', views.evaluacion_itf_edit, name='evaluacion_itf_edit'),
    path('evaluacion_itf/delete/<int:pk>', views.evaluacion_itf_delete, name='evaluacion_itf_delete'),
]