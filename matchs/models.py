from django.db import models
from django.contrib.auth.models import User
from tournament.models import tournament
from player.models import team,player
# Create your models here.

class matchs(models.Model):
    match_id=models.AutoField(primary_key=True)
    tournament_id=models.ForeignKey(tournament,on_delete=models.PROTECT)
    team1_id=models.ForeignKey(team,on_delete=models.PROTECT,related_name="team1")
    team2_id=models.ForeignKey(team,on_delete=models.PROTECT)
    date_time=models.DateField()
    winner=models.IntegerField(default=0)

    def __str__(self) -> str:
        s = f"{self.team1_id}vs{self.team2_id}"
        return s

class score(models.Model):
    player_id=models.ForeignKey(player,on_delete=models.PROTECT)
    match_id=models.ForeignKey(matchs,on_delete=models.PROTECT)
    kils = models.IntegerField(default=0)
    
