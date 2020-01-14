from rest_framework import routers
from olympics import views

router = routers.DefaultRouter()
router.register(r'sports', views.SportViewset)
router.register(r'events', views.EventViewset)
router.register(r'olympics', views.OlympicViewset)
router.register(r'teams', views.TeamViewset)
router.register(r'athletes', views.AthleteViewset)
router.register(r'olympicEvents', views.OlympicEventViewset)