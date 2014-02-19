from django.contrib.auth import login
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
    form = AuthenticationForm()
  return render(request, "accounts/form.html", {"form": form})

def logoutView(request):
  user = User.objects.get(username=request.user)
  if user not None:
    logout(user)
    return HttpResponseRedirect('/accounts/login/')
  return HttpResponseRedirect('/accounts/login/')

def newUser(request):
  print request.user
  if request.method == "POST":
    form = UserCreationForm(request.POST)
    if form.is_valid():
      new_user = form.save()
      login(new_user)
      return HttpResponseRedirect("/char_sheet/")
  else:
    form = UserCreationForm()
  return render(request, "accounts/form.html", {"form": form})


