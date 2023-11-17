from django.urls import path
from . import views

app_name = 'proyectotf'

urlpatterns = [
    path('listaptf/', views.proyectotf_list, name='proyectotf_list'),
    path('nuevo/', views.proyectotf_create, name='proyectotf_create'),
    path('<int:pk>/', views.proyectotf_detail, name='proyectotf_detail'),
    path('ptf_delete/<int:pk>/', views.proyectotf_delete, name='proyectotf_delete'),
    path('ptf_edit/<int:pk>/', views.proyectotf_edit, name='proyectotf_edit'),
    path('ptf_edit_miembros/<int:pk>/', views.proyectotf_miembro_edit, name='proyectotf_miembro_edit'),
    path('nuevo_miembros/', views.proyectotf_miembros_create, name='proyectotf_miembros_create'),
    ###
    path('listaitf/', views.informetf_list, name='informetf_list'),
    path('nuevoitf/', views.informetf_create, name='informetf_create'),
    path('itf/<int:pk>', views.informetf_detail, name='informetf_detail'),
    path('itf_delete/<int:pk>/', views.informetf_delete, name='informetf_delete'),
    path('itf_edit/<int:pk>/', views.informetf_edit, name='informetf_edit'),
]