from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class organiser(models.Model):
    organiser_id=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)

    def __str__(self) -> str:
        return self.organiser_id.username
