#!/usr/bin/env python

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celero.settings')

import django
django.setup()

import pandas as pd
# from celero.celero.olympics.model import Sport, Event, Olympic, Team, Athlete, OlympicEvent
from olympics.models import Sport, Event, Olympic, Team, Athlete, OlympicEvent

def main():
#    read_noc_regions()
    read_athlete_events()

def read_athlete_events():
    athlete_events = pd.read_csv("../data/athlete_events.csv")
    # print(athlete_events)
    #read_sports(athlete_events)
    # read_events(athlete_events)
    read_games(athlete_events)
    
def read_sports(df):
    print("\t- Reading Sports")
    for name, group in df.groupby("Sport"):
        Sport.objects.create(name = name)

def read_events(df):
    print("\t- Reading Sports")
    order_sport = df.sort_values("Sport")
    sport_name = None
    sport = None
    for name, group in order_sport.groupby("Event"):
        current_sport = group["Sport"].iloc[0]
        if sport_name == None or sport_name != current_sport:
            sport_name = current_sport
            sport = Sport.objects.get(name = sport_name)
        Event.objects.create(name = name, sport = sport)

def read_games(df):
    print("\t- Reading Olympic Games")
    for name, group in df.groupby("Games"):
        print(group["Year"])
        print(group["Season"].iloc[0])

        print(group["City"].iloc[0])
        Olympic.objects.create(year=group["Year"].iloc[0], season=group["Season"].iloc[0],
            city=group["City"].iloc[0])

def read_noc_regions():
    noc_regions = pd.read_csv("../data/noc_regions.csv")
    for row in noc_regions.rows:
        Team.objects.create(noc = row["NOC"], name = row["regions"], notes = row["notes"])
        team.save()

if __name__ == "__main__":
    main()