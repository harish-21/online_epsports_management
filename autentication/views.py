from datetime import date
from django.shortcuts import render , redirect
from django.contrib.auth.models import User,Group
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages 
from django.http import JsonResponse
from tournament.models import tournament
from player.models import team , player
from matchs.models import score,matchs
from creater.models import organiser
from json import dumps

#sorting function
def sorting(list):
    n = len(list)
    for i in range(n-1):
        for j in range(0,n-i-1):
            if list[j][1]<list[j+1][1]:
                list[j],list[j+1] = list[j+1],list[j]
    
    num=5
    if n<num:
        num = n
    
    dict = []
    
    for i in range(num):
        t = {}
        t['n'] = i+1
        t['name'] = list[i][0]
        t['points'] = list[i][1]
        dict.append(t)

    return dict
        

# This will be the view for home page for players
def index(request):
    return render(request,"index.html")

def divert(request):
    if request.user.is_authenticated:
       return redirect('tournament/tourlist')

def divert2(request):
    if request.user.is_authenticated:
       return redirect('admin/tournament/tournament/add/')


def autenticate(request):
    return render(request,"autenticate.html")

def notpermitted(request):
    return render(request,"not_permitted.html")

def signout(request):
    logout(request)
    return redirect('autenticate')

def registration(request):
    if request.method == "POST":
        username= request.POST.get('username')
        fname = request.POST.get('fname') 
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        if pass1 == pass2:
            user = User.objects.create_user(username,email,pass1)
            user.first_name = fname
            user.last_name = lname
            user.save()
            my_group = Group.objects.get(name='Players') 
            my_group.user_set.add(user)

            user = authenticate(username=username,password=pass1)

            if user is not None:
                login(request,user)
            
            return redirect("index")

    return redirect("notpermitted")

def tourinfo(request):
    return render(request,"playerlist.html")

def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['pass']

        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            group = Group(name="Organisers")
            creator = User.objects.get(id=request.user.id)
            if creator.groups.filter(name=group):
                return redirect("organiserdashboard")

            group = Group(name="Players")
            creator = User.objects.get(id=request.user.id)
            if creator.groups.filter(name=group):
                if player.objects.get(player_id=creator):
                    return redirect("playerdashboard")
            
                return redirect("index")

    return redirect("autenticate")

def playerdashboard(request):
    if request.user.is_authenticated:
        temp = User.objects.get(id=request.user.id)
        info = player.objects.get(player_id=temp)
        teaminfo = player.objects.get(player_id=info)
        tid = teaminfo.team_id
        data = {"win":tid.wins,"losses":tid.losses}
        tinfo = dumps(data)
        players = player.objects.filter(team_id=tid)

        data = score.objects.filter(player_id=info)
        n = len(data)
        scores=0
        for i in range(n):
            scores += data[i].kils

        dic = player.objects.get(player_id=info)
        dic.player_score = scores
        dic.no_of_matchs = n
        dic.save()

        return render(request,"dashboard.html",{'players':players,'n':n,'kills':scores,'teams':tinfo})

# def playsomething(request,id):
#     if request.user.is_authenticated:
#         # if player.objects.filter(player_id = request.user.id).exists():
#         #     teams = team.objects.get(team_id=)
#         teams = team.objects.filter(tournament_id = id)
#         return render(request,"playershome.html",{'teams':teams})

# def organisesomething(request):
#     if request.user.is_authenticated:
#         return redirect("tournament/addtournament")

def divert3(request):
    if request.user.is_authenticated:
        return redirect("admin/player/team/add/")

def organiserdashboard(request):
    if request.user.is_authenticated:
        group = Group(name="Organisers")
        creator = User.objects.get(id=request.user.id)
        if creator.groups.filter(name=group):
            org = organiser.objects.get(organiser_id=creator)
            tour = tournament.objects.filter(organiser_id=org)
            team_deter = []
            teams=[]
            for i in tour:
               t = team.objects.filter(tournament_id=i)
               for j in t:
                   t_list = [j.team_name,j.points]
                   team_deter.append(j)
                   teams.append(t_list)
            teams = sorting(teams)
            print(team_deter)
            players=[]
            for i in team_deter:
                 p = player.objects.filter(team_id=i)
                 for k in p:
                    p_value = [k.player_id,k.player_score]
                    players.append(p_value)
            players = sorting(players)
    
           
            
            return render(request,"organiserdashboard.html",{'tour':tour,'teams':teams,'players':players})

def organiserinput(request,id):
    tour = tournament.objects.get(tournament_id=id)
    teams = team.objects.filter(tournament_id=tour)
    if request.method == "POST":
        t1id = request.POST['team1_id']
        t2id = request.POST['team2_id']
        if t1id == t2id:
            messages.error(request,"Teams cannot be same")
            return redirect('organiserinput',id=id)
        else:
            team1 = team.objects.get(team_id=t1id)
            team2 = team.objects.get(team_id=t2id)
            winner = request.POST["winner_id"]
            if t1id == winner:
                team1.wins = team1.wins + 1
                team1.points = team1.wins*2
                team2.losses = team2.losses + 1
                team1.save()
                team2.save()
            else:
                team2.wins = team2.wins + 1
                team2.points = team2.wins*2
                team1.losses = team1.losses + 1
                team2.save()
                team1.save()

            matchday = date.today()
            info = matchs(tournament_id=tour,team1_id=team1,team2_id=team2,date_time=matchday,winner=winner)
            info.save()

            players1 = player.objects.filter(team_id=t1id)
            players2 = player.objects.filter(team_id=t2id)
            for i in players1:
                kills = request.POST[str(i.player_id.id)]
                data = score(player_id=i,match_id = info,kils = kills)
                data.save()

            for i in players2:
                kills = request.POST[str(i.player_id.id)]
                data = score(player_id=i,match_id = info,kils = kills)
                data.save()

            players = player.objects.all()
            for i in players:
                scores = score.objects.filter(player_id=i)
                sum = 0
                for j in scores:
                    a = j.kils
                    sum = sum + a
                i.player_score = sum
                i.no_of_matchs = len(scores)
                i.save()
        return redirect('organiserdashboard')
            

    else:
        tour = tournament.objects.get(tournament_id=id)
        teams = team.objects.filter(tournament_id=tour)

        

        
    return render(request,"organiserinput.html",{'tour':tour,'tourid':id,'teams':teams})


def get_topics_ajax(request):
    if request.method == "POST":
        tid = request.POST['tid']
        data=[]
        try:
            players = player.objects.filter(team_id = tid)

            for i in players:
                info = {'name':i.player_id.username,"id":i.player_id.id}
                data.append(info)

        except Exception:
             data['error_message'] = 'error'
             return JsonResponse(data)
        return JsonResponse(data, safe = False) 

def jointeam(request):
    teams = team.objects.all()
    data =[]
    for i in teams:
        if i.no_players < 3:
            data.append(i)
    return render (request,"jointeam.html",{'data':data})

def allowjoin(request,id):
    uid = User.objects.get(id=request.user.id)
    tid = team.objects.get(team_id=id)
    info = player(player_id=uid,team_id=tid)
    info.save()
    return redirect("playerdashboard")










