from  rest_framework import serializers
from base.models import MatchDetail, Match, Team, Section, SectionName, Stage,StageName, Tournament

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields='__all__'

class StageNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = StageName
        fields = ['stage_name_name']

class SectionNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = SectionName
        fields = ['section_name']
    
class TournamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tournament
        fields = '__all__'

class StageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stage
        fields = '__all__'
    stage_name = StageNameSerializer(many=False)
    tournament_id = TournamentSerializer(many=False)

class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = '__all__'

    section_name = SectionNameSerializer(many=False)
    stage_id = StageSerializer(many=False)

class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = '__all__'

    section_id = SectionSerializer(many=False)
    
class MatchDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = MatchDetail
        fields = '__all__'

    match_id = MatchSerializer(many=False)
    team_id = TeamSerializer(many=False)
    
