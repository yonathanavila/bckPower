from django.urls import path

from . import views

urlpatterns = [
    path("league", views.index, name="index"),
    path("set/tournaments", views.SetTournaments, name="Set Tournaments"),
    path("set/teams", views.SetTeams, name="Set Teams"),
    path("set/players", views.SetPlayersJson, name="Set Players"),
    path("set/game/info", views.SetGameInfo, name="Set Game Info"),
    path("set/game/detail", views.SetGameDetail.as_view(), name="Set Game Detail"),
    path("league/all", views.getAllLeagues, name="getAllLeagues")
]