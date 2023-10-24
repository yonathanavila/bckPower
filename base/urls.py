from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("download", views.DownloadData.as_view(), name="My Data Downloaded"),
    path("<int:tournament_id>/", views.SetLeague, name=""),
    path("set/league", views.SetLeague, name="Set Leagues"),
    path("set/tournament", views.SetTournaments, name="Set Tournaments"),
    path("set/team", views.SetTeams, name="Set Teams"),
    path("set/player", views.SetPlayers, name="Set Players"),
    path("set/gamedetail", views.SetGameDetail.as_view(), name="Set Game Detail"),
    path("league/all", views.getAllLeagues, name="getAllLeagues"),
    path("set/stage", views.SetStagesAndSection.as_view(), name="Set Stage"),
    path("set/game", views.SetGame.as_view(), name="Set Game"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
