from django.urls import path
from .views import AlumnoList, AlumnoCreate

app_name = 'persona'

urlpatterns = [

    #alumno views
    path('alumno/', AlumnoList.as_view(), name='alumno_list'),
    path('alumno/nuevo/', AlumnoCreate.as_view(), name='alumno_create'),
    #path('alumno/<int:pk>/', views.alumno_detail, name='alumno_detail'),
    #path('alumno_delete/<int:pk>/', views.alumno_delete, name='alumno_delete'),
    #path('alumno_edit/<int:pk>/',views.alumno_edit, name='alumno_edit'),

    #docente views
    """
    path('docente/', views.docente_list, name='docente_list'),
    path('docente/nuevo/', views.docente_create, name='docente_create'),
    path('docente/<int:pk>/', views.docente_detail, name='docente_detail'),
    path('docente_delete/<int:pk>/', views.docente_delete, name='docente_delete'),
    path('docente_edit/<int:pk>/',views.docente_edit, name='docente_edit'),
    """

    """
    #asesor views
    path('asesor/', views.asesor_list, name='asesor_list'),
    path('asesor/nuevo/', views.asesor_create, name='asesor_create'),
    path('asesor/<int:pk>/', views.asesor_detail, name='asesor_detail'),
    path('asesor_delete/<int:pk>/', views.asesor_delete, name='asesor_delete'),
    path('asesor_edit/<int:pk>/',views.asesor_edit, name='asesor_edit'),

    #login views
    path('', views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout")
    """

]