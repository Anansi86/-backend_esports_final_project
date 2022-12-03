from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    #custom_field = models.CharField(blank=True, max_length=60)
    custom_field = 0

class Match(models.Model):
    win = models.CharField(max_length=25, blank=False, unique=True)
    video_url = models.TextField()
    created = models.DateTimeField()
    updated = models.DateTimeField()
    status = models.IntegerField()
#    team1 = models.ForeignKey(Team,on_delete=models.SET_NULL, null=True, related_name="Team1")
#   team2 = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, related_name="Team2")
    status = models.IntegerField()
#    score = models.ForeignKey('Match_score', on_delete=models.SET_NULL, null=True, related_name="score") # '' because Match_score is after match