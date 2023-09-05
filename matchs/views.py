from django.shortcuts import render
from .forms import matchform
from player.models import player
from .models import matchs,score

# Create your views here.
def addmatch(request):
    if request.method == "POST":
        form = matchform(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = matchform()
    
    return render(request,"matchform.html",{'form':form})

def playerinfo(request,id):
    info = score.objects.filter(player_id=id)
    n = len(info)
    scores=0
    for i in range(n):
        scores += info[i].kill

    dic = player.objects.get(player_id=id)
    dic.player_score = scores
    dic.no_of_matchs = n
    dic.save()
    
    return render(request, "dashboard.html",{'n':n,'kills':scores}) 

def addinfo(request):
    pass

def playerinfo(request):
    return render(request,"tournamentinfo.html")
    
    


