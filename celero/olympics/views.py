from django.shortcuts import render
from olympics import models
from olympics import serializers
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework import viewsets

class SportViewset(viewsets.ModelViewSet):
    queryset = models.Sport.objects.all()
    serializer_class = serializers.SportSerializer

    def get_queryset(self):
        queryset = models.Sport.objects.all()
        # Check if a parameters was passed to get
        if self.request.query_params:
            # Check if the parameter name is in models fields
            if "name" in self.request.query_params:
                queryset = queryset.filter(name__contains=self.request.query_params["name"])

        return queryset

class EventViewset(viewsets.ModelViewSet):
    queryset = models.Event.objects.all()
    serializer_class = serializers.EventSerializer

    def get_queryset(self):
        queryset = models.Event.objects.all()
        # Check if a parameters was passed to get
        if self.request.query_params:
            # Check if the parameter name is in models fields
            if "name" in self.request.query_params:
                queryset = queryset.filter(name__contains=self.request.query_params["name"])
            if "sport" in self.request.query_params:
                queryset = queryset.filter(sport=self.request.query_params["sport"])

        return queryset

class OlympicViewset(viewsets.ModelViewSet):
    queryset = models.Olympic.objects.all()
    serializer_class = serializers.OlympicSerializer

    def get_queryset(self):
        queryset = models.Olympic.objects.all()
        # Check if a parameters was passed to get
        if self.request.query_params:
            # Check if the parameter name is in models fields
            if "year" in self.request.query_params:
               queryset = queryset.filter(year=self.request.query_params["year"])
            if "season" in self.request.query_params:
                if self.request.query_params["season"] == "Summer":
                    queryset = queryset.filter(season="S")
                elif self.request.query_params["season"] == "Winter":
                    queryset = queryset.filter(season="W")
            if "city" in self.request.query_params:
                queryset = queryset.filter(city__contains=self.request.query_params["city"])
        return queryset

class TeamViewset(viewsets.ModelViewSet):
    queryset = models.Team.objects.all()
    serializer_class = serializers.TeamSerializer

    def get_queryset(self):
        queryset = models.Team.objects.all()
        # Check if a parameters was passed to get
        if self.request.query_params:
            # Check if the parameter name is in models fields
            if "noc" in self.request.query_params:
               queryset = queryset.filter(noc=self.request.query_params["noc"])
            if "name" in self.request.query_params:
                    queryset = queryset.filter(name__contains=self.request.query_params["name"])
            if "notes" in self.request.query_params:
                queryset = queryset.filter(notes__contains=self.request.query_params["notes"])
        return queryset

class AthleteViewset(viewsets.ModelViewSet):
    queryset = models.Athlete.objects.all()
    serializer_class = serializers.AthleteSerializer

    def get_queryset(self):
        queryset = models.Athlete.objects.all()
        # Check if a parameters was passed to get
        if self.request.query_params:
            # Check if the parameter name is in models fields
            if "name" in self.request.query_params:
                queryset = queryset.filter(name__contains=self.request.query_params["name"])
            if "team" in self.request.query_params:
                queryset = queryset.filter(team=self.request.query_params["team"])
            if "sex" in self.request.query_params:
                if self.request.query_params["sex"] == "Male":
                    queryset = queryset.filter(sex="M")
                elif self.request.query_params["sex"] == "Female":
                    queryset = queryset.filter(sex="F")
        return queryset

class OlympicEventViewset(viewsets.ModelViewSet):
    queryset = models.OlympicEvent.objects.all()
    serializer_class = serializers.OlympicEventSerializer

    def get_queryset(self):
        queryset = models.OlympicEvent.objects.all()
        # Check if a parameters was passed to get
        if self.request.query_params:
            # Check if the parameter name is in models fields
            if "event" in self.request.query_params:
                queryset = queryset.filter(event=self.request.query_params["event"])
            if "olympic" in self.request.query_params:
                queryset = queryset.filter(olympic=self.request.query_params["olympic"])
            if "athlete" in self.request.query_params:
                queryset = queryset.filter(athlete=self.request.query_params["athlete"])
            if "age" in self.request.query_params:
                queryset = queryset.filter(age=self.request.query_params["age"])
            if "weight" in self.request.query_params:
                queryset = queryset.filter(weight=self.request.query_params["weight"])
            if "height" in self.request.query_params:
                queryset = queryset.filter(height=self.request.query_params["height"])
            if "medal" in self.request.query_params:
                if self.request.query_params["medal"] == "Gold":
                    queryset = queryset.filter(medal="G")
                elif self.request.query_params["medal"] == "Silver":
                    queryset = queryset.filter(medal="S")
                elif self.request.query_params["medal"] == "Bronze":
                    queryset = queryset.filter(medal="B")
        return queryset