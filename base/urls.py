from django.urls import path
from base import views

urlpatterns = [
    path("",views.index, name="home"),
    path("evening",views.eveningPlayers, name="evening")
]
