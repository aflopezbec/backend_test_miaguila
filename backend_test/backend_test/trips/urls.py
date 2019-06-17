from django.urls import path
from backend_test.trips.views import countTrips, TripView
from rest_framework_mongoengine import routers

router = routers.DefaultRouter()
router.register(r'trips', TripView)

urlpatterns = [
]

urlpatterns += router.urls

apiTripsPatterns = ([
    path('trips/count/', countTrips , name='count'),

]+router.urls, 'api_trips')