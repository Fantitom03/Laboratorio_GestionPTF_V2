from django.urls import path
from . import views

app_name = 'proyectotf'

urlpatterns = [
    path('lista/', views.proyectotf_list, name='proyectotf_list'),
    path('nuevo/', views.proyectotf_create, name='proyectotf_create'),
    path('<int:pk>/', views.proyectotf_detail, name='proyectotf_detail'),
    path('delete/<int:pk>/', views.proyectotf_delete, name='proyectotf_delete'),
    path('edit/<int:pk>/', views.proyectotf_edit, name='proyectotf_edit'),
    path('nuevo_miembros/', views.proyectotf_miembros_create, name='proyectotf_miembros_create'),
]