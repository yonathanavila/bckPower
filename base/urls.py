from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("<int:tournament_id>/", views.SetLeague, name=""),
    path("set/league", views.SetLeague, name="Set Leagues"),
    path("set/tournament", views.SetTournaments, name="Set Tournaments"),
    path("set/team/<int:year>", views.SetTeams, name="Set Teams"),
    path("set/player", views.SetPlayersJson, name="Set Players"),
    path("set/game/info", views.SetGameInfo, name="Set Game Info"),
    path("set/game/detail", views.SetGameDetail.as_view(), name="Set Game Detail"),
    path("league/all", views.getAllLeagues, name="getAllLeagues"),
    path("open/game/<int:year>/name/<slug:game>/item/<int:item>", views.openGameJson, name="Open Games"),
    path("set/stage", views.SetStagesAndSection.as_view(), name="Set Stage"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
