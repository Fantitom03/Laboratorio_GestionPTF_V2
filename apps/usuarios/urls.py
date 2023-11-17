from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = 'usuarios'

urlpatterns = [
    path("", views.index, name="index"),
    path("home", TemplateView.as_view(template_name='usuario.html'), name="usuario"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    #path("registro", views.register, name="registro")
]
