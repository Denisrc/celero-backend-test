from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, APITestCase
from olympics.models import Sport, Event, Olympic

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
        # Get sport with id 2
        response = self.client.get("/api/olympics/1/")
        response_data = response.data
        
        olympic = response_data

        self.assertEquals(olympic["id"], 1)
        self.assertEquals(olympic["year"], 2020)
        self.assertEquals(olympic["season"], "S")
        self.assertEquals(olympic["city"], "City A")

        # Get sport with id 2
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
