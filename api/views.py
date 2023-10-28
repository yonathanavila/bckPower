import ast
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
        try:
            listTeam = []
            listQuerysetMoreMatchDetail = []
            groupPhases = ["Groups", "Play In Groups"]
            stage = request.query_params.get("stage")
            if not stage:
                return Response(
                    {"message": "Your tournament id or stage are incorrect"},
                    status=status.HTTP_404_NOT_FOUND,
                )

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
        except Exception as e:
            return Response(
                    {"message": str(e)},
                    status=status.HTTP_404_NOT_FOUND,
                )

class RankingGlobalStatsView(APIView):
    def get(self, request):
        try:
            listQuerysetMoreMatchDetail = [];
            avoidRepitedTeam = [];

            numberOfTeams = int(request.query_params.get("number_of_teams")) or 20;
            if not numberOfTeams:
                return Response(
                    {"message": "Your number of teams are incorrect format!"},
                    status=status.HTTP_404_NOT_FOUND,
                )

            querysetTeam = Team.objects.all();

            for team in querysetTeam:

                gameXTeam = MatchDetail.objects.filter(team_id__team_id__exact=team.team_id);

                # Count win/loses
                win = 0
                lose = 0
                for game in gameXTeam:
                    if game.match_detail_win:
                        win += 1
                    else:
                        lose += 1

                listQuerysetMoreMatchDetail.append(
                    {
                        "team_id": team.team_id,
                        "team_code": team.team_acronym,
                        "team_name": team.team_name,
                        "win": win,
                        "lose": lose,
                        "played": win + lose,
                    }
                )
                avoidRepitedTeam.append(team.team_id);

            # Calculate rankings based on wins
            rankings = sorted(
                listQuerysetMoreMatchDetail,
                key=lambda x: (x["win"], -x["played"]),
                reverse=True,
            )

            # cut the list based in the numberOfTeams requested
            rankings = rankings[:numberOfTeams];

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
            return Response(rankings_with_positions, status=status.HTTP_200_OK);
    
        except Exception as e:
            return Response(
                {"message": str(e)},
                status=status.HTTP_404_NOT_FOUND,
            )

class RankingTeamStatsView(APIView):
    def get(self, request):
        
        try:
        
            listQuerysetMoreMatchDetail = [];
            team_ids = request.query_params.get("team_ids") ;
          
            if not team_ids or not len(team_ids)>1:
                return Response(
                    {"message": "Your team ids array are incorrect"},
                    status=status.HTTP_404_NOT_FOUND,
                )

            teams =  ast.literal_eval(team_ids);

            for team_id in set(teams):
                queryTeam = Team.objects.get(team_id=team_id);
                gameXTeam = MatchDetail.objects.filter(team_id__team_id__exact=team_id);

                if not queryTeam or not gameXTeam:
                    return Response(
                        {"message": "Your team ids array are incorrect"},
                        status=status.HTTP_404_NOT_FOUND,
                    )

                # Count win/loses
                win = 0
                lose = 0
                for game in gameXTeam:
                    if game.match_detail_win:
                        win += 1
                    else:
                        lose += 1

                listQuerysetMoreMatchDetail.append(
                    {
                        "team_id":team_id,
                        "team_code": queryTeam.team_acronym,
                        "team_name": queryTeam.team_name,
                        "win": win,
                        "lose": lose,
                        "played": win + lose,
                    }
                )

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

            return Response(rankings_with_positions, status=status.HTTP_200_OK);
    
        except Exception as e:
            return Response(
                {"message": str(e)},
                status=status.HTTP_404_NOT_FOUND,
            )
