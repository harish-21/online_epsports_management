from django.db import models
#from player.models import team 
from creater.models import organiser

# Create your models here.
class tournament(models.Model):
    tournament_id=models.AutoField(primary_key=True)
    organiser_id=models.ForeignKey(organiser,on_delete=models.PROTECT)
    tournament_name=models.CharField(max_length=20,unique=True)
    game=models.CharField(max_length=20)
    winner_prize=models.IntegerField(default=0)
    runner_prize=models.IntegerField(default=0)
    entry_fee=models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.tournament_name

    