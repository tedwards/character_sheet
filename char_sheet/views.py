from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

from char_sheet.models import Characters
from character_sheet.DND4Eparser import *
from xml.dom import minidom
from .forms import UploadFileForm

def displayCharacter(request, character_id):
  character = Characters.objects.get(pk=character_id)
  context = {'character': character}
  return render(request, 'char_sheet/sheet.html', context)

@login_required
def userView(request):
  user = User.objects.get(username=request.user)
  characters = Characters.objects.filter(user=user)
  return render(request, 'char_sheet/char_list.html', {"user":user,"characters":characters})

@login_required
def deleteCharacter(request, character_id):
  character = Characters.objects.get(pk=character_id)
  character.delete()
  return HttpResponseRedirect('/char_sheet/')

@login_required
def createCharacter(request):
  if request.method == 'POST':
    form = UploadFileForm(request.POST, request.FILES)
    if form.is_valid():
      dom = minidom.parse(request.FILES['file'])
      details = handleDetails(dom.getElementsByTagName("Details")[0])
      stats = handleStats(dom.getElementsByTagName("Stat"))
      if details["Experience"]:
        experience = int(details["Experience"]),
      else:
        experience = 0

      character = Characters(
          user               = User.objects.get(username=request.user),
          name               = str(details["name"]),
          xp                 = int(experience),
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
      return HttpResponseRedirect('/char_sheet/')
  else:
    form = UploadFileForm()
  return render(request, "char_sheet/upload.html", {"form": form})


