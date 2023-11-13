from django.urls import path
from . import views

app_name = 'comision'

urlpatterns = [
    # URLs para MiembroCSTF
    path('cstf/', views.miembrocstf_list, name='cstf_list'),
    path('cstf/nuevo/', views.miembrocstf_create, name='cstf_create'),
    path('cstf/<int:pk>/', views.miembrocstf_detail, name='cstf_detail'),
    path('cstf_delete/<int:pk>/', views.miembrocstf_delete, name='cstf_delete'),
    path('cstf_edit/<int:pk>/', views.miembrocstf_edit, name='cstf_edit'),

    # URLs para MiembrosTE
    path('miembrote/', views.miembro_te_list, name='miembrote_list'),
    path('miembrote/nuevo/', views.miembro_te_create, name='miembrote_create'),
    path('miembrote/<int:pk>/', views.miembro_te_detail, name='miembrote_detail'),
    path('miembrote_delete/<int:pk>/', views.miembro_te_delete, name='miembrote_delete'),
    path('miembrote_edit/<int:pk>/', views.miembro_te_edit, name='miembrote_edit'),

    # URLs para TribunalEvaluador
    path('tribunal/', views.tribunal_list, name='tribunal_list'),
    path('tribunal/nuevo/', views.tribunal_create, name='tribunal_create'),
    path('tribunal/<int:pk>/', views.tribunal_detail, name='tribunal_detail'),
    path('tribunal_delete/<int:pk>/', views.tribunal_delete, name='tribunal_delete'),
    path('tribunal_edit/<int:pk>/', views.tribunal_edit, name='tribunal_edit'),
]