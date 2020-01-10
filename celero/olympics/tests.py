from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, APITestCase
from olympics.models import Sport

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