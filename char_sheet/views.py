# Create your views here.
from django.http import HttpResponse
from django.core.files import File
from django.conf import settings
from django.shortcuts import render

from char_sheet.models import Characters, Users
from character_sheet.DND4Eparser import *
from xml.dom import minidom

import os 

def index(request):
  return HttpResponse("Character Sheet Working")

def createCharacter(request):
  f = open(os.path.join(settings.PROJECT_ROOT,"ImmeralLvl3.dnd4e"))
  dom = minidom.parse(f)
  details = handleDetails(dom.getElementsByTagName("Details")[0])
  stats = handleStats(dom.getElementsByTagName("Stat"))

  character = Characters(
      user               = Users.objects.get(pk=1),
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
  return HttpResponse("Character %s created." % (str(details["name"])))

def displayCharacter(request):
  character = Characters.objects.get(pk=1)

  context = {'character': character}

  return render(request, 'char_sheet/sheet.html', context)
