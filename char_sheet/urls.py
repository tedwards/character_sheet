from django.conf.urls import patterns, url

from char_sheet import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^createCharacter/', views.createCharacter, name="createCharacter"),
    )

