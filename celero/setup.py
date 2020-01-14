#!/usr/bin/env python

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celero.settings')
import sys
import django
django.setup()
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist  
import pandas as pd
import numpy as np
# from celero.celero.olympics.model import Sport, Event, Olympic, Team, Athlete, OlympicEvent
from olympics.models import Sport, Event, Olympic, Team, Athlete, OlympicEvent

MEDAL_MAP = {
    "Gold": "G",
    "Silver": "S",
    "Bronze": "B"
}

def main():
    print("Populating Database")
    read_noc_regions()
    read_athlete_events()
    print("Done")

def read_athlete_events():
    athlete_events = None
    if len(sys.argv) > 1:
        nrows = int(sys.argv[1])
        athlete_events = pd.read_csv("../data/athlete_events.csv", nrows=nrows)
    else:
        athlete_events = pd.read_csv("../data/athlete_events.csv")
    
    read_sports(athlete_events)
    read_events(athlete_events)
    read_games(athlete_events)
    read_athletes(athlete_events)
    read_athletes_events(athlete_events)
    
def read_sports(df):
    print("\t- Reading Sports")
    for name, group in df.groupby("Sport"):
        try:
            sport = Sport.objects.create(name = name)
            sport.save()
        except IntegrityError:
            continue
        except:
            print("Error trying to create Event with: {}".format(name))
            continue

def read_events(df):
    print("\t- Reading Events")
    order_sport = df.sort_values("Sport")
    sport_name = None
    sport = None
    for name, group in order_sport.groupby("Event"):
        try:
            current_sport = group["Sport"].iloc[0]
            if sport_name == None or sport_name != current_sport:
                sport_name = current_sport
                sport = Sport.objects.get(name = sport_name)
            event = Event.objects.create(name = name, sport = sport)
            event.save()
        except IntegrityError:
            continue
        except:
            print("Error trying to create Event with: {}".format(group["Sport"].iloc[0]))
            continue

def read_games(df):
    print("\t- Reading Olympic Games")
    for name, group in df.groupby("Games"):
        try:
            olympic = Olympic.objects.create(year=group["Year"].iloc[0], season=group["Season"].iloc[0],
                city=group["City"].iloc[0])
            olympic.save()
        except IntegrityError:
            continue
        except:
            print("Error trying to create Olympic with: {}, {}, {}".format(group["Year"].iloc[0], group["Season"].iloc[0], group["City"].iloc[0]))
            continue
        
def read_athletes(df):
    print("\t- Reading Athletes")
    order_noc = df.sort_values("NOC")
    id_grouped = order_noc.groupby("ID")
    team = None
    counter = 0
    athlete_list = []
    grouped_size = id_grouped.size().shape[0]
    for name, group in id_grouped:
        if counter % 2000 == 0 and counter != 0:
            print("\t\t- Created {} of {} athletes".format(counter, grouped_size))
        counter += 1
        try:
            current_noc = group["NOC"].iloc[0]
            if team is None or team.noc != current_noc:
                try:
                    team = Team.objects.get(noc = current_noc)
                except ObjectDoesNotExist:
                    team = Team.objects.create(noc = current_noc, name = group["Team"].iloc[0])
                    team.save()
            athlete_list.append(Athlete(id=name, name=group["Name"].iloc[0], sex=group["Sex"].iloc[0], team = team))
        except IntegrityError:
            continue
        except:
            print("Error trying to create Athlete with: {}, {}".format(group["Name"].iloc[0], group["Sex"].iloc[0]))
            continue
    Athlete.objects.bulk_create(athlete_list)
        

def read_athletes_events(df):
    print("\t- Reading Athletes Events")
    size = df.shape[0]
    counter = 0
    athlete_events = []
    for index, row in df.iterrows():
        if counter % 2000 == 0 and counter != 0:
            print("\t\t- Created {} of {} Athletes Events".format(counter, size))
        counter += 1
        try:
            medal = None
            age = None
            weight = None
            height = None
            if str(row["Medal"]) != "nan":
                medal = MEDAL_MAP[row["Medal"]]
            athlete = Athlete.objects.get(id=row["ID"])
            event = Event.objects.get(name=row["Event"])
            olympic = Olympic.objects.get(year=row["Year"], season=row["Season"])

            if str(row["Age"]) != "nan":
                age = row["Age"]
            if str(row["Weight"]) != "nan":
                weigth = row["Weight"]
            if str(row["Height"]) != "nan":
                height = row["Height"]
            #olympic_event = OlympicEvent.objects.create(weight=weight, height=height, age=age, medal=medal)
            #olympic_event.save()
            athlete_events.append(OlympicEvent(weight=weight, height=height, age=age, medal=medal, 
                athlete=athlete, event=event, olympic=olympic))

        except ObjectDoesNotExist:
            continue   
        except IntegrityError:
            continue
        #except:
        #    print("Error trying to create Athlete Events with: {}, {}, {}, {}".format(row["ID"], row["Name"], row["Year"], row["Event"]))
        #     continue
    OlympicEvent.objects.bulk_create(athlete_events)

def read_noc_regions():
    print("\t- Reading NOC Regions")
    noc_regions = pd.read_csv("../data/noc_regions.csv")
    for index, row in noc_regions.iterrows():
        try:
            team = Team.objects.create(noc = row["NOC"], name = row["region"], notes = row["notes"])
            team.save()
        except IntegrityError:
            continue
        except:
            print("Errot trying to create Team with: {}".format(row["NOC"]))
            continue

if __name__ == "__main__":
    main()