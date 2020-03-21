from django.db import models
from django.utils.timezone import now

# Create your models here.

class RoadMap(models.Model):
    r_name = models.CharField(max_length=200, unique=True,verbose_name="nom du la RoadMap")
    r_durree = models.IntegerField(null=True,blank=True,verbose_name="Duree de chaque sprint en jours")
    r_dateDebut = models.DateTimeField(default=now)
    def __str__(self):
        return self.r_name

class SujetTraite(models.Model):
    s_name = models.CharField(max_length=200, unique=True,verbose_name="intitulé du sujet")
    s_durree = models.IntegerField(default=1,verbose_name="Nombre de sprint du sujet")
    s_sprintDebut = models.IntegerField(default=1,verbose_name="Sprint de debut du sujet")
    s_RoadMap = models.ForeignKey(RoadMap, on_delete=models.PROTECT,related_name="s_roadMaps")
    s_is_utile = models.BooleanField(default=False,verbose_name="Sprint blanc") 
    def __str__(self):
        return self.s_name+" du sprint "+str(self.s_sprintDebut)+" pendant "+str(self.s_durree)+" sprint"