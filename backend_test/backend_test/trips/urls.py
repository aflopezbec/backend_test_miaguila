from django.urls import path
from backend_test.trips.views import countTrips

apiTripsPatterns = ([
    path('count-trips/', countTrips , name='count_trips'),

], 'api_trips')