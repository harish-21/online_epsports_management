from django.urls import path
from . import views

urlpatterns = [
    path('addorganiser', views.addorganiser,name="addorganiser"),
]
