from django.db import models

# Create your models here.
class Sport(models.Model):
    sport_name=models.CharField(max_length=100,primary_key=True)
class players(models.Model):
    sport_name=models.ForeignKey(Sport,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    url=models.URLField()
class tornament(models.Model):
    name=models.ForeignKey(players,on_delete=models.CASCADE)
    date=models.DateField()
