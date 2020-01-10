from rest_framework import routers
from olympics import views

router = routers.DefaultRouter()
router.register(r'sports', views.SportViewset)