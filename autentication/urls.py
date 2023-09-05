from django.urls import path,include
from django.contrib import admin
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index',views.index,name="index"),
    path('playerdashboard',views.playerdashboard,name="playerdashboard"),
    path('autenticate',views.autenticate,name="autenticate"),
    path('registration', views.registration,name="registration"),
    path('organiserdashboard',views.organiserdashboard,name="organiserdashboard"),
    path('organiserinput/<int:id>',views.organiserinput,name="organiserinput"),
    path('signin',views.signin,name="signin"),
    path('get-topics-ajax/', views.get_topics_ajax, name="get_topics_ajax"),
    path('signout',views.signout,name="signout"),
    path('divert',views.divert,name="divert"),
    path('divert2',views.divert2,name="divert2"),
    path('divert3',views.divert3,name="divert3"),
    # path('playsomething/<int:id>',views.playsomething,name="playsomething"),
    # path('organisesomething',views.organisesomething,name="organisesomething"),
    path('jointeam',views.jointeam,name="jointeam"),
    path('allowjoin/<int:id>',views.allowjoin,name="allowjoin"),
    path('notpermitted',views.notpermitted,name="notpermitted"),
    path('tournament/',include('tournament.urls')),
    path('player/',include('player.urls')),
]
