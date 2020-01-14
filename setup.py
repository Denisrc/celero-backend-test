#!/usr/bin/env python
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celero.settings')

import django
django.setup()

import pandas as pd

from olympics import Sport, Event, Olympic, Team, Athlete, OlympicEvent

def main():
#    read_noc_regions()
    read_athlete_events()

def read_athlete_events():
    athlete_events = pd.read_csv("../data/athlete_events.csv")
    athlete_events.groupby["Sport"]

def read_noc_regions():
    noc_regions = pd.read_csv("../data/noc_regions.csv")
    for row in noc_regions.rows:
        Team.objects.create(noc = row["NOC"], name = row["regions"], notes = row["notes"])
        team.save()

if __name__ == "__main__":
    main()