from django.shortcuts import render
from olympics.models import Sport
from olympics.serializers import SportSerializer
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework import viewsets

class SportViewset(viewsets.ModelViewSet):
    queryset = Sport.objects.all()
    serializer_class = SportSerializer