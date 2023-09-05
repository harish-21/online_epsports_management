import imp
from django.db import models
from django.contrib.auth.models import User

from tournament.models import tournament

# Create your models here.
class team(models.Model):
    team_id=models.AutoField(primary_key=True)
    captain_id=models.ForeignKey(User,on_delete=models.PROTECT)
    team_name=models.CharField(max_length=20,unique=True)
    tournament_id=models.ForeignKey(tournament,on_delete=models.PROTECT)
    game=models.CharField(max_length=20)
    no_players=models.IntegerField(null=False,blank=False)
    points=models.IntegerField(default=0)
    wins=models.IntegerField(default=0)
    losses=models.IntegerField(default=0)
    draws=models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.team_name


class player(models.Model):
    player_id=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    team_id=models.ForeignKey(team,on_delete=models.PROTECT)
    player_score=models.IntegerField(default=0)
    no_of_matchs=models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.player_id.username


class invitation(models.Model):
    player_id=models.OneToOneField(User,on_delete=models.PROTECT,primary_key=True)
    coplayer_id=models.ForeignKey(User,on_delete=models.PROTECT,related_name="coplayer")
    status = models.BooleanField(default=False)

