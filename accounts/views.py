from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render

def index(request):
  return render(request, "accounts/index.html")

def loginView(request):
  request.session.set_test_cookie()
  if request.method == "POST":
    form = AuthenticationForm(request, request.POST)
    if form.is_valid():
      login(request, form.get_user())
      return HttpResponseRedirect("/char_sheet/")
    else:
      return HttpResponseRedirect("/char_sheet/")
  else:
    form = AuthenticationForm()
    new_user = True
  return render(request, "accounts/form.html", {"form": form, "new_user": new_user})

def logoutView(request):
  logout(request)
  return HttpResponseRedirect('/accounts/login/')

def newUser(request):
  if request.method == "POST":
    form = UserCreationForm(request.POST)
    if form.is_valid():
      new_user = form.save()
      return HttpResponseRedirect("/char_sheet/")
  else:
    form = UserCreationForm()
  return render(request, "accounts/form.html", {"form": form})
