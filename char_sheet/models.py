from django.db import models

# Create your models here.

class Users(models.Model):
  user = models.CharField(max_length=30, unique=True)

class Characters(models.Model):
  # char info
  user                = models.ForeignKey(Users)
  name                = models.CharField(max_length=50)
  xp                  = models.PositiveIntegerField()
  level               = models.PositiveIntegerField()
  death_save_count    = models.PositiveSmallIntegerField()
  healing_surges      = models.PositiveSmallIntegerField()
  hit_points          = models.SmallIntegerField()
  action_points       = models.PositiveSmallIntegerField()

  # abilities
  strength            = models.PositiveSmallIntegerField()
  constitution        = models.PositiveSmallIntegerField()
  dexterity           = models.PositiveSmallIntegerField()
  intelligence        = models.PositiveSmallIntegerField()
  wisdom              = models.PositiveSmallIntegerField()
  charisma            = models.PositiveSmallIntegerField()
  strength_mod        = models.SmallIntegerField()
  constitution_mod    = models.SmallIntegerField()
  dexterity_mod       = models.SmallIntegerField() 
  intelligence_mod    = models.SmallIntegerField()
  wisdom_mod          = models.SmallIntegerField()
  charisma_mod        = models.SmallIntegerField()

  #defenses
  ac                  = models.PositiveSmallIntegerField()
  fortitude           = models.PositiveSmallIntegerField()
  reflex              = models.PositiveSmallIntegerField()
  will                = models.PositiveSmallIntegerField()

  #Skills
  acrobatics          = models.SmallIntegerField()
  arcana              = models.SmallIntegerField()
  athletics           = models.SmallIntegerField()
  bluff               = models.SmallIntegerField()
  diplomacy           = models.SmallIntegerField()
  dungeoneering       = models.SmallIntegerField()
  endurance           = models.SmallIntegerField()
  heal                = models.SmallIntegerField()
  history             = models.SmallIntegerField()
  insight             = models.SmallIntegerField()
  intimidate          = models.SmallIntegerField()
  nature              = models.SmallIntegerField()
  perception          = models.SmallIntegerField()
  religion            = models.SmallIntegerField()
  stealth             = models.SmallIntegerField()
  streetwise          = models.SmallIntegerField()
  thievery            = models.SmallIntegerField()

  # combat stats and senses
  initiative          = models.SmallIntegerField()
  passive_insight     = models.PositiveSmallIntegerField()
  passive_perception  = models.PositiveSmallIntegerField()
  speed               = models.PositiveSmallIntegerField()
