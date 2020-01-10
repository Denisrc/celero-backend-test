from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, APITestCase
from olympics.models import Sport, Event

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
        
