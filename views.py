from django.shortcuts import render
from .models import *
from django.http import JsonResponse
import datetime
import pandas as pd
import numpy as np
from datetime import timedelta, datetime, tzinfo
# Create your views here.

def home(request):
    """
    Point d"entree de l'application, rend la vue
    """
    return render(request,"roadmap/home.html")

def getRessources(request):
    """
    Resultat d'un appel ajax
    Sert a recurerer la liste des ressources
    """
    resResource=[]
    for ressource in SujetTraite.objects.all().order_by("s_sprintDebut"):
            dicoRessource={}
            dicoRessource["id"]=ressource.id
            dicoRessource["title"]=ressource.s_name
            resResource.append(dicoRessource)
    return JsonResponse(resResource,safe=False)



def getEvents(request):
    """
    Resultat d'un appel ajax
    Sert a recurerer la liste des evenements du fullCalendar
    """
    resEvent=[]        
    for sujetTraite in SujetTraite.objects.all().order_by("s_sprintDebut"):
        date=sujetTraite.s_RoadMap.r_dateDebut
        dicoEvent={}
        dicoEvent["resourceId"]=sujetTraite.id
        dicoEvent["title"]=sujetTraite.s_name
        if sujetTraite.s_sprintDebut == 1:
            dicoEvent["start"]=sujetTraite.s_RoadMap.r_dateDebut.strftime('%Y-%m-%d')
        else: 
            dicoEvent["start"]=ajouteSiWeek(date, sujetTraite.s_RoadMap.r_durree*(sujetTraite.s_sprintDebut-1) )
        dicoEvent["end"]=ajouteSiWeek(date, sujetTraite.s_RoadMap.r_durree*(sujetTraite.s_sprintDebut-1)+(sujetTraite.s_RoadMap.r_durree*sujetTraite.s_durree) )
        if sujetTraite.s_is_utile:
            dicoEvent["color"]='lightblue'
        resEvent.append(dicoEvent)
    return JsonResponse(resEvent,safe=False)

def ajouteSiWeek(date,nombre):
    """
    fonction utiliser dans getEvents
    prend en parametre une date et un nombre de jour
    ajoute le nombre de jour indiqué dans nombre a la date en excluant le resultat le weekend
    """
    compteur=1
    for i in range(0,nombre):
        day=date + timedelta(days=compteur)
        if day.weekday()<=4:
            date=day
            compteur=1
        else:
            compteur+=1
    return date.strftime('%Y-%m-%d')