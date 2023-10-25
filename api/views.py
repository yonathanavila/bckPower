from base.models import MatchDetail, Team
from .serializers import MatchDetailSerializer
from django.core import serializers
from django.db.models import (
    Q,
    F,
    Subquery,
    IntegerField,
    ExpressionWrapper,
    DateTimeField,
)
from rest_framework import status, filters, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from datetime import timedelta
from dateutil.relativedelta import relativedelta


class RankingStatsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MatchDetail.objects.all()
    serializer_class = MatchDetailSerializer

    filter_backends = [DjangoFilterBackend, filters.SearchFilter]

    search_fields = ["idMatch__idSection__idStage__name"]

    filterset_fields = {"idMatch__idSection__idStage__name": ["exact"]}
    ordering_fields = ["idMatch"]


class RankingStatsView(APIView):
    def get(self, request, idTournament, format=None):
        listTeam = []
        listQuerysetMoreMatchDetail = []
        groupPhases = ["Groups", "Play In Groups"]
        stage = request.query_params.get("stage")
        print(stage)
        if not stage in groupPhases:
            queryset = MatchDetail.objects.filter(
                # match_detail_match_team_integrant=True,
                match_id__section_id__stage_id__stage_name__stage_name_name__contains=stage,
                match_id__section_id__stage_id__tournament_id__tournament_id__exact=idTournament,
            )
        else:
            queryset = MatchDetail.objects.filter(
                Q(
                    match_id__section_id__stage_id__stage_name__stage_name_name__contains=groupPhases[
                        0
                    ]
                )
                | Q(
                    match_id__section_id__stage_id__stage_name__stage_name_name__contains=groupPhases[
                        1
                    ]
                ),
                match_detail_match_team_integrant=True,
                match_id__section_id__stage_id__tournament_id__tournament_id__exact=idTournament,
            )

        if not queryset:
            return Response(
                {"message": "Your tournament id or stage are incorrect"},
                status=status.HTTP_404_NOT_FOUND,
            )
        serializer = MatchDetailSerializer(queryset, many=True)
        for data in serializer.data:
            for key, value in data.items():
                if key == "team_id":
                    print(dict(value))
                    data = dict(value)
                    data = {
                        "team_id": data["team_id"],
                        "team_code": data["team_acronym"],
                        "team_name": data["team_name"],
                        "rank": 1,
                    }
                    listTeam.append(data)
        avoidRepitedTeam = []
        for team in listTeam:
            if not team['team_id'] in avoidRepitedTeam:
                six_months_ago = timedelta(
                    days=30 * 6
                )  # Assuming an average of 30 days per month

                # Calculate the datetime for 6 months ago relative to the time of the query
                six_months_ago_datetime = ExpressionWrapper(
                    F(
                        "match_id__section_id__stage_id__tournament_id__tournament_start_date"
                    )
                    - six_months_ago,
                    output_field=DateTimeField(),
                )

                moreGameXTeam = MatchDetail.objects.filter(
                    team_id__team_id__exact=team['team_id'],
                    match_id__section_id__stage_id__tournament_id__tournament_start_date__gt=six_months_ago_datetime,
                )


                # Count win/loses
                win = 0
                lose = 0
                for game in moreGameXTeam:
                    if game.match_detail_win:
                        win += 1
                    else:
                        lose += 1
                listQuerysetMoreMatchDetail.append(
                    {
                        "team_id": team["team_id"],
                        "team_code": team["team_code"],
                        "team_name": team["team_name"],
                        "win": win,
                        "lose": lose,
                        "played": win + lose,
                    }
                )
                avoidRepitedTeam.append(team['team_id']);
        
        # Calculate rankings based on wins
        rankings = sorted(
            listQuerysetMoreMatchDetail,
            key=lambda x: (x["win"], -x["played"]),
            reverse=True,
        )

        # Add positions (ranks) to each item
        rankings_with_positions = list(
            map(
                lambda x: {
                    "team_id": x[1]["team_id"],
                    "team_code": x[1]["team_code"],
                    "team_name": x[1]["team_name"],
                    "rank": x[0] + 1,
                },
                enumerate(rankings),
            )
        )
        print("Ranking: ", rankings_with_positions)
        return Response(rankings_with_positions, status=status.HTTP_200_OK)


class RankingGlobalStatsView(APIView):
    def get(self, request):
        numberOfTeams = request.query_params.get("number_of_teams") or 20
        queryset = []
        serializer = MatchDetailSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class RankingTeamStatsiView(APIView):
    def get(self, request):
        numberOfTeams = request.query_params.get("team_rankings") or 20
        queryset = []
        serializer = MatchDetailSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
