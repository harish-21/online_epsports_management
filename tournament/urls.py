from django.urls import path,include
from . import views

urlpatterns = [
    path('addtournament', views.addtournament,name="addtournament"),
    path('tourinfo/<int:id>', views.tourinfo,name="tourinfo"),
    path('teaminfo/<int:id>',views.teaminfo,name="teaminfo"),
    path('registerteam',views.registerteam,name='registerteam'),
    path('tourlist',views.tourlist,name="tourlist"),
    
]
