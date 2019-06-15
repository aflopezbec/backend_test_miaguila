from django.urls import path
from backend_test.trips.views import countTrips, TripView

apiTripsPatterns = ([
    path('trips/', TripView.as_view() , name='trips-list'),
    path('trips/count', countTrips , name='count_trips'),

], 'api_trips')