from  rest_framework import serializers
from base.models import MatchDetail, MatchStrategy, Match, Team, Section, SectionName, Stage,StageName, Tournament

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields= ['team_id','team_name', 'team_acronym', 'team_slug']

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
        fields = ['tournament_id', 'tournament_name', 'tournament_slug', 'tournament_sport', 'tournament_start_date', 'tournament_end_date']

class StageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stage
        fields = ['tournament_id', 'stage_name', 'stage_type', 'stage_slug']
    stage_name = StageNameSerializer(many=False)
    tournament_id = TournamentSerializer(many=False)

class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = ['section_name', 'stage_id']

    section_name = SectionNameSerializer(many=False)
    stage_id = StageSerializer(many=False)

class MatchStrategy(serializers.ModelSerializer):
    class Meta:
        model = MatchStrategy
        fields = ['match_strategy_name']

class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = ['match_type', 'match_state', 'match_mode', 'match_strategy', 'section_id']

    section_id = SectionSerializer(many=False)
    match_strategy = MatchStrategy(many=False)

class MatchDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = MatchDetail
        fields = ['match_id','match_detail_win', 'team_id']

    match_id = MatchSerializer(many=False)
    team_id = TeamSerializer(many=False)
    
