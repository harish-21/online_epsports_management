from django.urls import path
from . import views

urlpatterns = [
    path('addmatch', views.addmatch,name="addmatch"),
    path('playerinfo/<int:id>',views.playerinfo,name="playerinfo"),

]
