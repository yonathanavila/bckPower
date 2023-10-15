from django.urls import path, include
from django.contrib import admin
from rest_framework import routers
from rankings import views

router = routers.DefaultRouter();
router.register("ranking", views.RankingStatsViewSet, basename="Ranking");

urlpatterns = [
    path("api/v1/ranking/tournament_rankings/<int:idTournament>/", views.RankingStatsView.as_view(), name="Get ranking by tournament"),
    path('api/v1/auth/', include('rest_framework.urls')),
    path("api/v1/data/", include("base.urls")),
    path("api/v1/", include(router.urls)),
    path("admin/", admin.site.urls),
];

