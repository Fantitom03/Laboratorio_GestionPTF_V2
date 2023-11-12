from django.urls import path
from apps.comision.views import MiembrosTE_List, MiembrosTE_Create

app_name = 'comision'

urlpatterns = [
    path('listarte/', MiembrosTE_List.as_view(), name='miembroTE_list'),
    path('miembrote/nuevo/', MiembrosTE_Create.as_view(), name='miembroTE_crear'),
    #path('miembrote/<int:pk>/', views.miembro_te_detail, name='miembrote_detail'),
    #path('miembrote_delete/<int:pk>/', views.miembro_te_delete, name='miembrote_delete'),
    #path('miembrote_edit/<int:pk>/', views.miembro_te_edit, name='miembrote_edit'),

]