from django.contrib.auth.models import User
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse



def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("usuarios:login"))
    return render(request, "usuario.html")


def login_view(request):
  if request.method == "POST":

    # Attempt to sign user in
    email = request.POST["email"]
    password = request.POST["password"]
    user = authenticate(request, username=email, password=password)

    # Check if authentication successful
    if user is not None:
      login(request, user)
      return HttpResponseRedirect(reverse("usuarios:usuario"))
    else:
      return render(request, "login.html", {
        "message": "Invalid email and/or password."
      })
  else:
    if request.user.is_authenticated:
      return HttpResponseRedirect(reverse("usuarios:usuario"))

    return render(request, "login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("usuarios:login"))



"""

def register(request):
  if request.method == "POST":
    email = request.POST["email"]


    # Ensure password matches confirmation
    password = request.POST["password"]
    confirmation = request.POST["confirmation"]
    if password != confirmation:
      return render(request, "register.html", {
        "message": "Passwords must match."
      })

    # Attempt to create new user
    try:
      user = User.objects.create_user(email, email, password)
      user.save()
    except IntegrityError as e:
      print(e)
      return render(request, "register.html", {
        "message": "Email address already taken."
      })
    login(request, user)
    return HttpResponseRedirect(reverse("usuarios:login"))
  else:
    return render(request, "register.html")

"""


