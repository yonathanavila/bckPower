from base.models import MatchDetail 
from .serializers import MatchDetailSerializer

from rest_framework import status, filters, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend

class RankingStatsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MatchDetail.objects.all();
    serializer_class = MatchDetailSerializer;
   
    filter_backends = [DjangoFilterBackend, filters.SearchFilter];

    search_fields = ['idMatch__idSection__idStage__name'];

    filterset_fields = {
        'idMatch__idSection__idStage__name': ['exact']
    };
    ordering_fields = ['idMatch'];

class RankingStatsView(APIView):
    def get(self, request, idTournament, format=None):
        stage =  request.query_params.get('stage');
        queryset = MatchDetail.objects.filter(
            matchTeamIntegrants=True, 
            idMatch__idSection__idStage__name__exact=stage,
            idMatch__idSection__idStage__idTournament__idTournament__exact=idTournament);
        if not queryset:
            return Response({'message':'Your tournament id or stage are incorrect'}, status=status.HTTP_404_NOT_FOUND);
        serializer = MatchDetailSerializer(queryset, many=True);
        return Response(serializer.data, status=status.HTTP_200_OK);

class RankingGlobalStatsView(APIView):
    def get(self, request):
        numberOfTeams = request.query_params.get('number_of_teams') or 20;
        queryset = []
        serializer = MatchDetailSerializer(queryset, many=True);
        return Response(serializer.data, status=status.HTTP_200_OK);

