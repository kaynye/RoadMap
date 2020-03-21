from django.conf.urls import include, url
from django.urls import path
from . import views


app_name = 'roadmap'
urlpatterns = [

    path('/', views.home,name="loginUser"),
    path('/getRessources/ ', views.getRessources,name="getRessources"),
    path('/getEvents/ ', views.getEvents,name="getEvents")
]