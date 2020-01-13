from django.shortcuts import render
from olympics import models
from olympics import serializers
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework import viewsets

class SportViewset(viewsets.ModelViewSet):
    queryset = models.Sport.objects.all()
    serializer_class = serializers.SportSerializer

class EventViewset(viewsets.ModelViewSet):
    queryset = models.Event.objects.all()
    serializer_class = serializers.EventSerializer

class OlympicViewset(viewsets.ModelViewSet):
    queryset = models.Olympic.objects.all()
    serializer_class = serializers.OlympicSerializer

class TeamViewset(viewsets.ModelViewSet):
    queryset = models.Team.objects.all()
    serializer_class = serializers.TeamSerializer

class AthleteViewset(viewsets.ModelViewSet):
    queryset = models.Athlete.objects.all()
    serializer_class = serializers.AthleteSerializer

class OlympicEventViewset(viewsets.ModelViewSet):
    queryset = models.OlympicEvent.objects.all()
    serializer_class = serializers.OlympicEventSerializer