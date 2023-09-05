from django.shortcuts import render,redirect
from django.contrib.auth.models import User,Group
from django.contrib import messages
from .forms import tournamentform
from .models import tournament
from player.models import player ,team
from creater.models import organiser
from json import dumps

# This feature is only accssed by organisers
def addtournament(request):
    if request.user.is_authenticated:
        group = Group(name="Organisers")
        creator = User.objects.get(id=request.user.id)
        if creator.groups.filter(name=group):
            if request.method == "POST":
                form = tournamentform(request.POST)
                if form.is_valid():
                    tname = form.cleaned_data['tournament_name']
                    game = form.cleaned_data['game']
                    wprize = form.cleaned_data['winner_prize']
                    rprize = form.cleaned_data['runner_prize']
                    efee = form.cleaned_data['entry_fee']
                    oid = User.objects.get(id=request.user.id)
                    organiser_info = organiser(organiser_id=oid)
                    organiser_info.save()
                    orid = organiser.objects.get(organiser_id=oid)
                    info = tournament(organiser_id=orid,tournament_name=tname,game=game,winner_prize=wprize,runner_prize=rprize, entry_fee=efee)
                    info.save()          
            else:
                form = tournamentform()
            return render(request,"tournamentform.html",{'form':form})
        else:
            return render(request,"not_permitted.html")
    else:
        messages.error(request,"Sign in or register to view this page.")
        return redirect("autentication/signin")

# Will contain the information about the tournament
def tourinfo(request,id):
    if request.user.is_authenticated:
        teams = team.objects.filter(tournament_id=id)
        return render(request,"tournamentinfo.html",{'teams':teams})
    else:
        return render(request,"not_permitted.html")


def registerteam(request):
    pass

def tourlist(request):
    if request.user.is_authenticated:
        tour = tournament.objects.all()
        return render(request,"tournamentlist.html",{'tour':tour})
    else:
        return render(request,"not_permitted.html")

def teaminfo(request,id):
    if request.user.is_authenticated:
        players = player.objects.filter(team_id=id)
        return render(request,"teaminfo.html",{'players':players})
    else:
        return render(request,"not_permitted.html")
    







    

        
