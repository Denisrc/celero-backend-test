from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, APITestCase
from olympics.models import Sport, Event, Olympic, Team, Athlete, OlympicEvent

class SportTestCase(APITestCase):
    
    def setUp(self):
        sport_name = "Sport 1"
        sport_name_2 = "Sport 2"

        sport = Sport.objects.create(name = sport_name)
        sport.save()

        sport_2 = Sport.objects.create(name = sport_name_2)
        sport_2.save()

        self.base_body = {
            "name": "New Sport"
        }

    # Test get all elements in list
    def test_sports_list_all(self):
        response = self.client.get("/api/sports/")
        response_data = response.data

        self.assertEquals(len(response_data), 2)

        sport = response_data[0]
        sport_2 = response_data[1]

        self.assertEquals(sport["id"], 1)
        self.assertEquals(sport["name"], "Sport 1")

        self.assertEquals(sport_2["id"], 2)
        self.assertEquals(sport_2["name"], "Sport 2")

    # Test get a empty list
    def test_sports_list_empty(self):
        Sport.objects.all().delete()
        response = self.client.get("/api/sports/")
        response_data = response.data

        self.assertEquals(len(response_data), 0)

    # Test fetching a sport by id
    def test_sports_get_by_id(self):
        # Get sport with id 2
        response = self.client.get("/api/sports/1/")
        response_data = response.data
        
        sport = response_data

        self.assertEquals(sport["id"], 1)
        self.assertEquals(sport["name"], "Sport 1")

        # Get sport with id 2
        response = self.client.get("/api/sports/2/")
        response_data = response.data

        sport = response_data

        self.assertEquals(sport["id"], 2)
        self.assertEquals(sport["name"], "Sport 2")

    # Test creating a new sport
    def test_create_new_sport(self):
        request = self.client.post("/api/sports/", self.base_body, format = "json")

        self.assertEquals(request.status_code, status.HTTP_201_CREATED)
        self.assertEquals(request.data['id'], 3)

        sport = Sport.objects.get(id=3)

        self.assertEquals(sport.name, 'New Sport')

    # Test update a sport using a PUT request
    def test_update_sport_put(self):
        sport = Sport.objects.get(id=1)
        self.assertEquals(sport.name, "Sport 1")

        request = self.client.put("/api/sports/1/", self.base_body, format = "json")

        self.assertEquals(request.status_code, status.HTTP_200_OK)

        sport = Sport.objects.get(id=1)

        self.assertEquals(sport.name, 'New Sport')

    # Test update a sport using a PATCH request
    def test_update_sport_patch(self):
        sport = Sport.objects.get(id=1)
        self.assertEquals(sport.name, "Sport 1")

        request = self.client.put("/api/sports/1/", self.base_body, format = "json")

        self.assertEquals(request.status_code, status.HTTP_200_OK)

        sport = Sport.objects.get(id=1)

        self.assertEquals(sport.name, 'New Sport')

    # Test update a sport using a PATCH request
    def test_delete_sport(self):
        sports = Sport.objects.all()

        self.assertEquals(len(sports), 2)

        request = self.client.delete("/api/sports/1/")

        self.assertEquals(request.status_code, status.HTTP_204_NO_CONTENT)

        sports = Sport.objects.all()

        self.assertEquals(len(sports), 1)

        self.assertEquals(sports[0].name, 'Sport 2')
        self.assertEquals(sports[0].id, 2)

class EventTestCase(APITestCase):
    def setUp(self):
        sport_name = "Sport 1"
        sport_name_2 = "Sport 2"

        sport = Sport.objects.create(name = sport_name)
        sport.save()

        sport_2 = Sport.objects.create(name = sport_name_2)
        sport_2.save()

        event = Event.objects.create(name = "Event 1.0", sport = sport)
        event.save()

        event_2 = Event.objects.create(name = "Event 2", sport = sport_2)
        event_2.save()

        event_3 = Event.objects.create(name = "Event 1.1", sport = sport)
        event_3.save()

        self.base_body = {
            "name": "New Event",
            "sport": 2
        }

    # Test get all elements in list
    def test_events_list_all(self):
        response = self.client.get("/api/events/")
        response_data = response.data

        self.assertEquals(len(response_data), 3)


        self.assertEquals(response_data[0]["id"], 1)
        self.assertEquals(response_data[0]["name"], "Event 1.0")
        self.assertEquals(response_data[0]["sport"], 1)
        

        self.assertEquals(response_data[1]["id"], 2)
        self.assertEquals(response_data[1]["name"], "Event 2")
        self.assertEquals(response_data[1]["sport"], 2)

    # Test get a empty list
    def test_events_list_empty(self):
        Event.objects.all().delete()
        response = self.client.get("/api/events/")
        response_data = response.data

        self.assertEquals(len(response_data), 0)

    # Test fetching an event by id
    def test_events_get_by_id(self):
        # Get event with id 2
        response = self.client.get("/api/events/1/")
        response_data = response.data
        
        event = response_data

        self.assertEquals(event["id"], 1)
        self.assertEquals(event["name"], "Event 1.0")
        self.assertEquals(event["sport"], 1)

        sport = Sport.objects.get(pk=event["sport"])

        self.assertEquals(sport.name, "Sport 1")
        # Get event with id 2
        response = self.client.get("/api/events/2/")
        response_data = response.data

        event = response_data

        self.assertEquals(event["id"], 2)
        self.assertEquals(event["name"], "Event 2")
        self.assertEquals(event["sport"], 2)

        sport = Sport.objects.get(pk=event["sport"])

        self.assertEquals(sport.name, "Sport 2")


        # Get event with id 3
        response = self.client.get("/api/events/3/")
        response_data = response.data

        event = response_data

        self.assertEquals(event["id"], 3)
        self.assertEquals(event["name"], "Event 1.1")
        self.assertEquals(event["sport"], 1)

        sport = Sport.objects.get(pk=event["sport"])

        self.assertEquals(sport.name, "Sport 1")

    # Test creating a new event
    def test_create_new_event(self):
        request = self.client.post("/api/events/", self.base_body, format = "json")

        self.assertEquals(request.status_code, status.HTTP_201_CREATED)
        self.assertEquals(request.data["id"], 4)

        event = Event.objects.get(id=4)

        self.assertEquals(event.name, "New Event")
        self.assertEquals(event.sport.name, "Sport 2")

    # Test update an event using a PUT request
    def test_update_event_put(self):
        event = Event.objects.get(id=1)
        self.assertEquals(event.name, "Event 1.0")
        self.assertEquals(event.sport.name, "Sport 1")

        request = self.client.put("/api/events/1/", self.base_body, format = "json")

        self.assertEquals(request.status_code, status.HTTP_200_OK)

        event = Event.objects.get(id=1)

        self.assertEquals(event.name, "New Event")
        self.assertEquals(event.sport.name, "Sport 2")

    # Test update an event using a PUT request, without passing all fields
    def test_update_event_put_error(self):
        event = Event.objects.get(id=1)
        self.assertEquals(event.name, "Event 1.0")
        self.assertEquals(event.sport.name, "Sport 1")

        body = {
            "name": "Event Error"
        }

        request = self.client.put("/api/events/1/", body, format = "json")

        self.assertEquals(request.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEquals(request.data["sport"][0], "This field is required.")

    # Test update an event using a PATCH request
    def test_update_event_patch(self):
        event = Event.objects.get(id=1)
        self.assertEquals(event.name, "Event 1.0")
        self.assertEquals(event.sport.name, "Sport 1")

        request = self.client.patch("/api/events/1/", self.base_body, format = "json")

        self.assertEquals(request.status_code, status.HTTP_200_OK)

        event = Event.objects.get(id=1)

        self.assertEquals(event.name, "New Event")
        self.assertEquals(event.sport.name, "Sport 2")

    # Test delete an event
    def test_delete_event(self):
        events = Event.objects.all()

        self.assertEquals(len(events), 3)

        request = self.client.delete("/api/events/1/")

        self.assertEquals(request.status_code, status.HTTP_204_NO_CONTENT)

        events = Event.objects.all()

        self.assertEquals(len(events), 2)

        self.assertEquals(events[0].name, 'Event 2')
        self.assertEquals(events[0].id, 2)

    # Test deleting a sport related with events, removing the events with cascade
    def test_delete_sport_cascade(self):
        events = Event.objects.all()
        sports = Sport.objects.all()

        self.assertEquals(len(events), 3)
        self.assertEquals(len(sports), 2)

        # Events with id 1 and 3 have the sport with id 1,
        # so both events also must be removed
        request = self.client.delete("/api/sports/1/")

        self.assertEquals(request.status_code, status.HTTP_204_NO_CONTENT)

        events = Event.objects.all()
        sports = Sport.objects.all()

        self.assertEquals(len(events), 1)
        self.assertEquals(len(sports), 1)

        self.assertEquals(events[0].name, "Event 2")
        self.assertEquals(events[0].id, 2)
        self.assertEquals(events[0].sport.name, "Sport 2")
        
class OlympicTestCase(APITestCase):
    
    def setUp(self):
        olympic = Olympic.objects.create(year = 2020, season = 'S', city = "City A")
        olympic.save()

        olympic_2 = Olympic.objects.create(year = 2020, season = 'W', city = "City B")
        olympic_2.save()

        self.base_body = {
            "year": 2030,
            "season": "Summer",
            "city": "City C"
        }

    # Test get all elements in list
    def test_olympics_list_all(self):
        response = self.client.get("/api/olympics/")
        response_data = response.data

        self.assertEquals(len(response_data), 2)

        olympic = response_data[0]
        olympic_2 = response_data[1]

        self.assertEquals(olympic["id"], 1)
        self.assertEquals(olympic["year"], 2020)
        self.assertEquals(olympic["season"], "S")
        self.assertEquals(olympic["city"], "City A")

        self.assertEquals(olympic_2["id"], 2)
        self.assertEquals(olympic_2["year"], 2020)
        self.assertEquals(olympic_2["season"], "W")
        self.assertEquals(olympic_2["city"], "City B")

    # Test get a empty list
    def test_sports_list_empty(self):
        Olympic.objects.all().delete()
        response = self.client.get("/api/olympics/")
        response_data = response.data

        self.assertEquals(len(response_data), 0)

    # Test fetching a olympic by id
    def test_olympics_get_by_id(self):
        # Get olympic with id 2
        response = self.client.get("/api/olympics/1/")
        response_data = response.data
        
        olympic = response_data

        self.assertEquals(olympic["id"], 1)
        self.assertEquals(olympic["year"], 2020)
        self.assertEquals(olympic["season"], "S")
        self.assertEquals(olympic["city"], "City A")

        # Get olympic with id 2
        response = self.client.get("/api/olympics/2/")
        response_data = response.data

        olympic_2 = response_data

        self.assertEquals(olympic_2["id"], 2)
        self.assertEquals(olympic_2["year"], 2020)
        self.assertEquals(olympic_2["season"], "W")
        self.assertEquals(olympic_2["city"], "City B")

    # Test creating a new olympic
    def test_create_new_olympic(self):
        request = self.client.post("/api/olympics/", self.base_body, format = "json")

        self.assertEquals(request.status_code, status.HTTP_201_CREATED)
        self.assertEquals(request.data['id'], 3)

        olympic = Olympic.objects.get(id=3)

        self.assertEquals(olympic.year, 2030)
        self.assertEquals(olympic.city, "City C")
        self.assertEquals(olympic.season, "Summer")

    # Test creating a new olympic with invalid season
    def test_create_new_olympic_invalid_season(self):
        base_body = self.base_body
        base_body["season"] = "Autumn"
        request = self.client.post("/api/olympics/", base_body, format = "json")

        self.assertEquals(request.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEquals(request.data["season"][0], '"Autumn" is not a valid choice.')

    # Test update a olympic using a PUT request
    def test_update_olympic_put(self):
        olympic = Olympic.objects.get(id=1)
        self.assertEquals(olympic.year, 2020)
        self.assertEquals(olympic.season, "S")
        self.assertEquals(olympic.city, "City A")

        request = self.client.put("/api/olympics/1/", self.base_body, format = "json")

        self.assertEquals(request.status_code, status.HTTP_200_OK)

        olympic = Olympic.objects.get(id=1)

        self.assertEquals(olympic.year, 2030)
        self.assertEquals(olympic.season, "Summer")
        self.assertEquals(olympic.city, "City C")

    # Test update a olympic using a PATCH request
    def test_update_olympic_patch(self):
        olympic = Olympic.objects.get(id=1)
        self.assertEquals(olympic.year, 2020)
        self.assertEquals(olympic.season, "S")
        self.assertEquals(olympic.city, "City A")

        request = self.client.put("/api/olympics/1/", self.base_body, format = "json")

        self.assertEquals(request.status_code, status.HTTP_200_OK)

        olympic = Olympic.objects.get(id=1)

        self.assertEquals(olympic.year, 2030)
        self.assertEquals(olympic.season, "Summer")
        self.assertEquals(olympic.city, "City C")

    # Test delete a olympic
    def test_delete_olympic(self):
        olympics = Olympic.objects.all()

        self.assertEquals(len(olympics), 2)

        request = self.client.delete("/api/olympics/1/")

        self.assertEquals(request.status_code, status.HTTP_204_NO_CONTENT)

        olympics = Olympic.objects.all()

        self.assertEquals(len(olympics), 1)

        self.assertEquals(olympics[0].year, 2020)
        self.assertEquals(olympics[0].city, "City B")
        self.assertEquals(olympics[0].id, 2)

class TeamTestCase(APITestCase):
    
    def setUp(self):
        team = Team.objects.create(noc = "ABC", name = "Name 1")
        team.save()

        team_2 = Team.objects.create(noc = "DEF", name = "Name 2")
        team_2.save()

        self.base_body = {
            "noc": "GHI",
            "name": "Name 3"
        }

    # Test get all elements in list
    def test_teams_list_all(self):
        response = self.client.get("/api/teams/")
        response_data = response.data

        self.assertEquals(len(response_data), 2)

        team = response_data[0]
        team_2 = response_data[1]

        self.assertEquals(team["id"], 1)
        self.assertEquals(team["noc"], "ABC")
        self.assertEquals(team["name"], "Name 1")

        self.assertEquals(team_2["id"], 2)
        self.assertEquals(team_2["noc"], "DEF")
        self.assertEquals(team_2["name"], "Name 2")

    # Test get a empty list
    def test_team_list_empty(self):
        Team.objects.all().delete()
        response = self.client.get("/api/teams/")
        response_data = response.data

        self.assertEquals(len(response_data), 0)

    # Test fetching a team by id
    def test_team_get_by_id(self):
        # Get team with id 2
        response = self.client.get("/api/teams/1/")
        response_data = response.data
        
        team = response_data

        self.assertEquals(team["id"], 1)
        self.assertEquals(team["noc"], "ABC")
        self.assertEquals(team["name"], "Name 1")

        # Get team with id 2
        response = self.client.get("/api/teams/2/")
        response_data = response.data

        team_2 = response_data

        self.assertEquals(team_2["id"], 2)
        self.assertEquals(team_2["noc"], "DEF")
        self.assertEquals(team_2["name"], "Name 2")

    # Test creating a new team
    def test_create_new_team(self):
        request = self.client.post("/api/teams/", self.base_body, format = "json")

        self.assertEquals(request.status_code, status.HTTP_201_CREATED)
        self.assertEquals(request.data['id'], 3)

        team = Team.objects.get(id=3)

        self.assertEquals(team.noc, "GHI")
        self.assertEquals(team.name, "Name 3")

    # Test creating a new team with nov with less than 3 characters
    def test_create_new_team_invalid_noc_less_than_3(self):
        base_body = self.base_body
        base_body["noc"] = "NO"
        request = self.client.post("/api/teams/", base_body, format = "json")

        self.assertEquals(request.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEquals(request.data["noc"][0], "Ensure this field has at least 3 characters.")

    # Test creating a new team with nov with more than 3 characters
    def test_create_new_team_invalid_noc_more_than_3(self):
        base_body = self.base_body
        base_body["noc"] = "NOCS"
        request = self.client.post("/api/teams/", base_body, format = "json")

        self.assertEquals(request.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEquals(request.data["noc"][0], "Ensure this field has no more than 3 characters.")

    # Test update a team using a PUT request
    def test_update_team_put(self):
        team = Team.objects.get(id=1)
        self.assertEquals(team.noc, "ABC")
        self.assertEquals(team.name, "Name 1")

        request = self.client.put("/api/teams/1/", self.base_body, format = "json")

        self.assertEquals(request.status_code, status.HTTP_200_OK)

        team = Team.objects.get(id=1)

        self.assertEquals(team.noc, "GHI")
        self.assertEquals(team.name, "Name 3")

    # Test update a team using a PATCH request
    def test_update_team_patch(self):
        team = Team.objects.get(id=1)
        self.assertEquals(team.noc, "ABC")
        self.assertEquals(team.name, "Name 1")

        request = self.client.put("/api/teams/1/", self.base_body, format = "json")

        self.assertEquals(request.status_code, status.HTTP_200_OK)

        team = Team.objects.get(id=1)

        self.assertEquals(team.noc, "GHI")
        self.assertEquals(team.name, "Name 3")

    # Test delete a team
    def test_delete_olympic(self):
        teams = Team.objects.all()

        self.assertEquals(len(teams), 2)

        request = self.client.delete("/api/teams/1/")

        self.assertEquals(request.status_code, status.HTTP_204_NO_CONTENT)

        teams = Team.objects.all()

        self.assertEquals(len(teams), 1)

        self.assertEquals(teams[0].name, "Name 2")
        self.assertEquals(teams[0].noc, "DEF")
        self.assertEquals(teams[0].id, 2)

class AthleteTestCase(APITestCase):
    
    def setUp(self):
        team = Team.objects.create(noc = "ABC", name = "Name 1")
        team.save()

        team_2 = Team.objects.create(noc = "DEF", name = "Name 2")
        team_2.save()

        athlete = Athlete.objects.create(name="Athlete 1", age=20, height=70, weight=180, sex="M", team=team)
        athlete.save()

        athlete_2 = Athlete.objects.create(name="Athlete 2", age=25, height=68, weight=170, sex="F", team=team_2)
        athlete_2.save()

        self.base_body = {
            "name": "Name",
            "age": 30,
            "height": 75,
            "weight": 175,
            "sex": "Male",
            "team": 1
        }

    # Test get all elements in list
    def test_athletes_list_all(self):
        response = self.client.get("/api/athletes/")
        response_data = response.data

        self.assertEquals(len(response_data), 2)

        athlete = response_data[0]
        athlete_2 = response_data[1]

        self.assertEquals(athlete["id"], 1)
        self.assertEquals(athlete["name"], "Athlete 1")
        self.assertEquals(athlete["age"], 20)
        self.assertEquals(athlete["height"], 70)
        self.assertEquals(athlete["weight"], 180)
        self.assertEquals(athlete["sex"], "M")
        self.assertEquals(athlete["team"], 1)

        self.assertEquals(athlete_2["id"], 2)
        self.assertEquals(athlete_2["name"], "Athlete 2")
        self.assertEquals(athlete_2["age"], 25)
        self.assertEquals(athlete_2["height"], 68)
        self.assertEquals(athlete_2["weight"], 170)
        self.assertEquals(athlete_2["sex"], "F")
        self.assertEquals(athlete_2["team"], 2)

    # Test get a empty list
    def test_team_list_empty(self):
        Athlete.objects.all().delete()
        response = self.client.get("/api/athletes/")
        response_data = response.data

        self.assertEquals(len(response_data), 0)

    # Test fetching a team by id
    def test_team_get_by_id(self):
        # Get team with id 2
        response = self.client.get("/api/athletes/1/")
        response_data = response.data
        
        athlete = response_data

        self.assertEquals(athlete["id"], 1)
        self.assertEquals(athlete["name"], "Athlete 1")
        self.assertEquals(athlete["age"], 20)
        self.assertEquals(athlete["height"], 70)
        self.assertEquals(athlete["weight"], 180)
        self.assertEquals(athlete["sex"], "M")
        self.assertEquals(athlete["team"], 1)

        # Get team with id 2
        response = self.client.get("/api/athletes/2/")
        response_data = response.data

        athlete_2 = response_data

        self.assertEquals(athlete_2["id"], 2)
        self.assertEquals(athlete_2["name"], "Athlete 2")
        self.assertEquals(athlete_2["age"], 25)
        self.assertEquals(athlete_2["height"], 68)
        self.assertEquals(athlete_2["weight"], 170)
        self.assertEquals(athlete_2["sex"], "F")
        self.assertEquals(athlete_2["team"], 2)

    # Test creating a new team
    def test_create_new_team(self):
        request = self.client.post("/api/athletes/", self.base_body, format = "json")

        self.assertEquals(request.status_code, status.HTTP_201_CREATED)
        self.assertEquals(request.data['id'], 3)

        athlete = Athlete.objects.get(id=3)

        self.assertEquals(athlete.name, "Name")
        self.assertEquals(athlete.age, 30)
        self.assertEquals(athlete.height, 75)
        self.assertEquals(athlete.weight, 175)
        self.assertEquals(athlete.sex, "Male")
        self.assertEquals(athlete.team.id, 1)

    # Test update a team using a PUT request
    def test_update_team_put(self):
        athlete = Athlete.objects.get(id=1)

        self.assertEquals(athlete.id, 1)
        self.assertEquals(athlete.name, "Athlete 1")
        self.assertEquals(athlete.age, 20)
        self.assertEquals(athlete.height, 70)
        self.assertEquals(athlete.weight, 180)
        self.assertEquals(athlete.sex, "M")
        self.assertEquals(athlete.team.id, 1)

        request = self.client.put("/api/athletes/1/", self.base_body, format = "json")

        self.assertEquals(request.status_code, status.HTTP_200_OK)

        athlete = Athlete.objects.get(id=1)

        self.assertEquals(athlete.name, "Name")
        self.assertEquals(athlete.age, 30)
        self.assertEquals(athlete.height, 75)
        self.assertEquals(athlete.weight, 175)
        self.assertEquals(athlete.sex, "Male")
        self.assertEquals(athlete.team.id, 1)

    # Test update a team using a PATCH request
    def test_update_team_patch(self):
        athlete = Athlete.objects.get(id=1)

        self.assertEquals(athlete.id, 1)
        self.assertEquals(athlete.name, "Athlete 1")
        self.assertEquals(athlete.age, 20)
        self.assertEquals(athlete.height, 70)
        self.assertEquals(athlete.weight, 180)
        self.assertEquals(athlete.sex, "M")
        self.assertEquals(athlete.team.id, 1)

        request = self.client.put("/api/athletes/1/", self.base_body, format = "json")

        self.assertEquals(request.status_code, status.HTTP_200_OK)

        athlete = Athlete.objects.get(id=1)

        self.assertEquals(athlete.name, "Name")
        self.assertEquals(athlete.age, 30)
        self.assertEquals(athlete.height, 75)
        self.assertEquals(athlete.weight, 175)
        self.assertEquals(athlete.sex, "Male")
        self.assertEquals(athlete.team.id, 1)

    # Test delete a team
    def test_delete_olympic(self):
        athletes = Athlete.objects.all()

        self.assertEquals(len(athletes), 2)

        request = self.client.delete("/api/athletes/1/")

        self.assertEquals(request.status_code, status.HTTP_204_NO_CONTENT)

        athletes = Athlete.objects.all()

        self.assertEquals(len(athletes), 1)

        self.assertEquals(athletes[0].id, 2)
        self.assertEquals(athletes[0].name, "Athlete 2")
        self.assertEquals(athletes[0].age, 25)
        self.assertEquals(athletes[0].height, 68)
        self.assertEquals(athletes[0].weight, 170)
        self.assertEquals(athletes[0].sex, "F")
        self.assertEquals(athletes[0].team.id, 2)

class OlympicEventTestCase(APITestCase):
    
    def setUp(self):
        sport = Sport.objects.create(name = "Sport 1")
        sport.save()

        sport_2 = Sport.objects.create(name = "Sport 2")
        sport_2.save()
        
        event = Event.objects.create(name = "Event 1", sport = sport)
        event.save()

        event_2 = Event.objects.create(name = "Event 2", sport = sport_2)
        event_2.save()

        team = Team.objects.create(noc = "ABC", name = "Name 1")
        team.save()

        team_2 = Team.objects.create(noc = "DEF", name = "Name 2")
        team_2.save()

        olympic = Olympic.objects.create(year = 2020, season = 'S', city = "City A")
        olympic.save()

        olympic_2 = Olympic.objects.create(year = 2020, season = 'W', city = "City B")
        olympic_2.save()

        athlete = Athlete.objects.create(name="Athlete 1", age=20, height=70, weight=180, sex="M", team=team)
        athlete.save()

        athlete_2 = Athlete.objects.create(name="Athlete 2", age=25, height=68, weight=170, sex="F", team=team_2)
        athlete_2.save()

        olympic_event = OlympicEvent.objects.create(event=event, olympic=olympic, athlete=athlete, medal=None)
        olympic_event.save()

        olympic_event_2 = OlympicEvent.objects.create(event=event_2, olympic=olympic_2, athlete=athlete_2, medal="S")
        olympic_event_2.save()

        self.base_body = {
            "event": 1,
            "olympic": 2,
            "athlete": 1,
            "medal": "Gold"
        }

    # Test get all elements in list
    def test_teams_list_all(self):
        response = self.client.get("/api/olympicEvents/")
        response_data = response.data

        self.assertEquals(len(response_data), 2)

        olympic_event = response_data[0]
        olympic_event_2 = response_data[1]

        self.assertEquals(olympic_event["id"], 1)
        self.assertEquals(olympic_event["medal"], None)
        self.assertEquals(olympic_event["event"], 1)
        self.assertEquals(olympic_event["olympic"], 1)

        self.assertEquals(olympic_event_2["id"], 2)
        self.assertEquals(olympic_event_2["medal"], "S")
        self.assertEquals(olympic_event_2["event"], 2)
        self.assertEquals(olympic_event_2["olympic"], 2)

    # Test get a empty list
    def test_team_list_empty(self):
        OlympicEvent.objects.all().delete()
        response = self.client.get("/api/olympicEvents/")
        response_data = response.data

        self.assertEquals(len(response_data), 0)

    # Test fetching a team by id
    def test_team_get_by_id(self):
        # Get team with id 2
        response = self.client.get("/api/olympicEvents/1/")
        response_data = response.data
        
        olympic_event = response_data

        self.assertEquals(olympic_event["id"], 1)
        self.assertEquals(olympic_event["medal"], None)
        self.assertEquals(olympic_event["event"], 1)
        self.assertEquals(olympic_event["olympic"], 1)

        # Get team with id 2
        response = self.client.get("/api/olympicEvents/2/")
        response_data = response.data

        olympic_event_2 = response_data

        self.assertEquals(olympic_event_2["id"], 2)
        self.assertEquals(olympic_event_2["medal"], "S")
        self.assertEquals(olympic_event_2["event"], 2)
        self.assertEquals(olympic_event_2["olympic"], 2)

    # Test creating a new team
    def test_create_new_team(self):
        request = self.client.post("/api/olympicEvents/", self.base_body, format = "json")

        self.assertEquals(request.status_code, status.HTTP_201_CREATED)
        self.assertEquals(request.data['id'], 3)

        olympic_event = OlympicEvent.objects.get(id=3)

        self.assertEquals(olympic_event.medal, "Gold")
        self.assertEquals(olympic_event.event.id, 1)
        self.assertEquals(olympic_event.olympic.id, 2)
        self.assertEquals(olympic_event.athlete.id, 1)

    # Test update a team using a PUT request
    def test_update_team_put(self):
        olympic_event = OlympicEvent.objects.get(id=1)

        self.assertEquals(olympic_event.id, 1)
        self.assertEquals(olympic_event.event.id, 1)
        self.assertEquals(olympic_event.athlete.id, 1)
        self.assertEquals(olympic_event.olympic.id, 1)

        request = self.client.put("/api/olympicEvents/1/", self.base_body, format = "json")

        self.assertEquals(request.status_code, status.HTTP_200_OK)

        olympic_event = OlympicEvent.objects.get(id=1)

        self.assertEquals(olympic_event.id, 1)
        self.assertEquals(olympic_event.event.id, 1)
        self.assertEquals(olympic_event.athlete.id, 1)
        self.assertEquals(olympic_event.olympic.id, 2)

    # Test update a team using a PATCH request
    def test_update_team_patch(self):        
        olympic_event = OlympicEvent.objects.get(id=1)
        
        self.assertEquals(olympic_event.id, 1)
        self.assertEquals(olympic_event.event.id, 1)
        self.assertEquals(olympic_event.athlete.id, 1)
        self.assertEquals(olympic_event.olympic.id, 1)

        request = self.client.put("/api/olympicEvents/1/", self.base_body, format = "json")

        self.assertEquals(request.status_code, status.HTTP_200_OK)

        olympic_event = OlympicEvent.objects.get(id=1)

        self.assertEquals(olympic_event.id, 1)
        self.assertEquals(olympic_event.event.id, 1)
        self.assertEquals(olympic_event.athlete.id, 1)
        self.assertEquals(olympic_event.olympic.id, 2)

    # Test delete a team
    def test_delete_olympic(self):
        olympic_event = OlympicEvent.objects.all()

        self.assertEquals(len(olympic_event), 2)

        request = self.client.delete("/api/olympicEvents/1/")

        self.assertEquals(request.status_code, status.HTTP_204_NO_CONTENT)

        olympic_event = OlympicEvent.objects.all()

        self.assertEquals(len(olympic_event), 1)

        self.assertEquals(olympic_event[0].id, 2)
        self.assertEquals(olympic_event[0].medal, "S")
        self.assertEquals(olympic_event[0].event.id, 2)
        self.assertEquals(olympic_event[0].olympic.id, 2)
