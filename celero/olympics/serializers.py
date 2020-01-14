from rest_framework import  serializers
from olympics.models import Sport, Event, Olympic, Team, Athlete, OlympicEvent

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
    notes =serializers.CharField(required=False, default=None, initial=None)
    class Meta:
        model = Team
        fields = ["id", "noc", "name", "notes"]

class AthleteSerializer(serializers.ModelSerializer):
    sex = serializers.ChoiceField(choices = {
        "Male": "M",
        "Female": "F"
    })

    class Meta:
        model = Athlete
        fields = ["id", "name", "sex", "team"]

class OlympicEventSerializer(serializers.ModelSerializer):
    medal = serializers.ChoiceField(choices= {
        "Gold": "G",
        "Silver": "S",
        "Bronze": "B"
    }, required=False, default=None, initial=None)

    class Meta:
        model = OlympicEvent
        fields = ["id", "medal", "event", "olympic", "athlete", "age", "height", "weight"]