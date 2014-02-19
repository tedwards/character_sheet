from django.conf.urls import patterns, url

from char_sheet import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^newUser/', views.newUser, name="newUser"),
    url(r'^login/', views.loginView, name="loginView"),
    url(r'^createCharacter/', views.createCharacter, name="createCharacter"),
    url(r'^displayCharacter/(?P<character_id>\d+)$', views.displayCharacter, name="displayCharacter"),
    )

