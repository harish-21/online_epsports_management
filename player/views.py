from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import teamform , playerform, invitationform
from .models import player,team
from creater.models import organiser
# Create your views here.

def addteam(request):
    if request.user.is_authenticated:
        print(organiser.objects.get(organiser_id = request.user.id))    
        if request.method == "POST":
            form = teamform(request.POST)
            if form.is_valid():
                tname = form.cleaned_data['team_name']
                game = form.cleaned_data['game']
                nop = form.cleaned_data['no_players']
                toid = form.cleaned_data['tournament_id']
                cid = User.objects.get(id=request.user.id)
                info = team(team_name=tname,game=game,no_players=nop,captain_id=cid,tournament_id=toid)
                info.save()
                tid = team.objects.get(captain_id=cid)
                player_info = player(player_id = cid,team_id=tid)
                player_info.save()

        else:
            form = teamform()
        return render(request,"playerform.html",{'form':form})
    else:
        messages.error(request,"Sign in or register to view this page.")
        return redirect("autentication/signin")


def addplayer(request):
    if request.method == "POST":
        form = playerform(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = playerform()
    
    return render(request,"playerform.html",{'form':form})

def invitation(request):
   form = invitationform()
   return render (request,"playerform.html",{'from':form})

def playerlist(request):
    ids=list(player.objects.values('player_id'))
    n = len(ids)
    names=[]
    teams=player.objects.values('team_id')
    matchs = player.objects.values('no_of_matchs')
    score = player.objects.values('player_score')
    for i in range(n):
       name = User.objects.get(id=ids[i]['player_id'])
       teamname = team.objects.get(team_id=teams[i]['team_id'])  
       names.append({'name':name,'id':ids[i]['player_id'],'team':teamname.team_name,
       'nom':matchs[i]['no_of_matchs'],'score':score[i]['player_score']})
    return render(request,"playerlist.html",{'names':names})

def playerinfo(request,id):
    pass