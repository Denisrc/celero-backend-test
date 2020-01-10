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

    season = serializers.ChoiceField(choices = {
        "Summer": "S",
        "Winter": "W"
    })

    class Meta:
        model = Olympic
        fields = ["id", "year", "season", "city"]