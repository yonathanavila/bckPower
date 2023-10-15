from  rest_framework import serializers
from base.models import MatchDetail

class MatchDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = MatchDetail
        fields = '__all__'
