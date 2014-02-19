# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.core.files import File
from django.conf import settings

from char_sheet.models import Characters
from character_sheet.DND4Eparser import *
from xml.dom import minidom
from forms import UserForm
import os 

@login_required
def userView(request):
  user = User.objects.get(username=request.user)
  characters = Characters.objects.filter(user=user)
  return render(request, 'char_sheet/char_list.html', {"user":user,"characters":characters})

@login_required
def createCharacter(request):
  if request.metohd == 'POST':
    form = UploadFileForm(request.POST, request.FILES)
    if form.is_valid():
      f = request.FILES['file']
      dom = minidom.parse(f)
      details = handleDetails(dom.getElementsByTagName("Details")[0])
      stats = handleStats(dom.getElementsByTagName("Stat"))

      character = Characters(
          user               = User.objects.get(username=request.user),
          name               = str(details["name"]),
          xp                 = int(details["Experience"]),
          level              = int(details["Level"]),
          death_save_count   = int(stats["Death Saves Count"]),
          healing_surges     = int(stats["Healing Surges"]),
          hit_points         = int(stats["Hit Points"]),
          action_points      = int(stats["_BaseActionPoints"]),
          strength           = int(stats["Strength"]),
          constitution       = int(stats["Constitution"]),
          dexterity          = int(stats["Dexterity"]),
          intelligence       = int(stats["Intelligence"]),
          wisdom             = int(stats["Wisdom"]),
          charisma           = int(stats["Charisma"]),
          strength_mod       = int(stats["Strength modifier"]),
          constitution_mod   = int(stats["Constitution modifier"]),
          dexterity_mod      = int(stats["Dexterity modifier"]),
          intelligence_mod   = int(stats["Intelligence modifier"]),
          wisdom_mod         = int(stats["Wisdom modifier"]),
          charisma_mod       = int(stats["Charisma modifier"]),
          ac                 = int(stats["AC"]),
          fortitude          = int(stats["Fortitude Defense"]),
          reflex             = int(stats["Reflex Defense"]),
          will               = int(stats["Will Defense"]),
          acrobatics         = int(stats["Acrobatics"]),
          arcana             = int(stats["Arcana"]),
          athletics          = int(stats["Athletics"]),
          bluff              = int(stats["Bluff"]),
          diplomacy          = int(stats["Diplomacy"]),
          dungeoneering      = int(stats["Dungeoneering"]),
          endurance          = int(stats["Endurance"]),
          heal               = int(stats["Heal"]),
          history            = int(stats["History"]),
          insight            = int(stats["Insight"]),
          intimidate         = int(stats["Intimidate"]),
          nature             = int(stats["Nature"]),
          perception         = int(stats["Perception"]),
          religion           = int(stats["Religion"]),
          stealth            = int(stats["Stealth"]),
          streetwise         = int(stats["Streetwise"]),
          thievery           = int(stats["Thievery"]),
          initiative         = int(stats["Initiative"]),
          passive_insight    = int(stats["Passive Insight"]),
          passive_perception = int(stats["Passive Perception"]),
          speed              = int(stats["Speed"]),
          )
      character.save()
    return HttpResponseRedirect('char_sheet/user/')
  else:
    form = UploadFileForm()
  return render(request, 'upload.html', {'form': form})

def displayCharacter(request, character_id):
  character = Characters.objects.get(pk=character_id)
  context = {'character': character}
  return render(request, 'char_sheet/sheet.html', context)
