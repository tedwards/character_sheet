from django.conf.urls import patterns, url

from accounts import views

urlpatterns = patterns('',
    url(r'^login/', views.loginView, name="login"),
    url('r/^logout/', views.logoutView, name="logout"),
    url(r"^createUser/", views.newUser, name="user")
    )

