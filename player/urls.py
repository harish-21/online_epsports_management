from django.urls import path,include
from . import views

urlpatterns = [
    path('addteam', views.addteam,name="addteam"),
    path('addplayer', views.addplayer,name="addplayer"),
    path('sendinvitation', views.invitation,name="sendinvitation"),
    path('playerlist',views.playerlist,name="playerlist"),
]
