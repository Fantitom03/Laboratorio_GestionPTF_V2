from django.urls import path
from apps.comision.views import MiembrosTE_List, MiembrosTE_Create, MiembrosTE_Detail, MiembrosTE_Eliminar, MiembrosTE_Editar

app_name = 'comision'

urlpatterns = [
    path('listarte/', MiembrosTE_List.as_view(), name='miembroTE_list'),
    path('miembrote/nuevo/', MiembrosTE_Create.as_view(), name='miembroTE_crear'),
    path('miembrote/<int:pk>/', MiembrosTE_Detail.as_view(), name='miembroTE_detalle'),
    path('miembrote_delete/<int:pk>/', MiembrosTE_Eliminar.as_view(), name='miembroTE_eliminar'),
    path('miembrote_edit/<int:pk>/', MiembrosTE_Editar.as_view(), name='miembroTE_editar'),

]