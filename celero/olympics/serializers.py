from rest_framework import  serializers
from olympics.models import Sport, Event, Olympic, Team, Athlete

class SportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sport
        fields = ["id", "name"]

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ["id", "name", "sport"]

class OlympicSerializer(serializers.ModelSerializer):
    games = serializers.SerializerMethodField()
    season = serializers.ChoiceField(choices = {
        "Summer": "S",
        "Winter": "W"
    })

    def get_games(self, obj):
        return str(obj.year) + ' ' + obj.season

    class Meta:
        model = Olympic
        fields = ["id", "year", "season", "city", "games"]

class TeamSerializer(serializers.ModelSerializer):
    noc = serializers.CharField(max_length=3, min_length=3)
    
    class Meta:
        model = Team
        fields = ["id", "noc", "name"]

class AthleteSerializer(serializers.ModelSerializer):
    sex = serializers.ChoiceField(choices = {
        "Male": "M",
        "Female": "F"
    })

    class Meta:
        model = Athlete
        fields = ["id", "name", "age", "height", "weight", "sex", "team"]