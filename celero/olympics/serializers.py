from rest_framework import  serializers
from olympics.models import Sport, Event, Olympic

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