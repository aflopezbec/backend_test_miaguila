from django.urls import path
from backend_test.trips.views import countTrips, TripView

apiTripsPatterns = ([
    path('count-trips/', countTrips , name='count_trips'),
    path('trips/', TripView.as_view() , name='trips-list'),

], 'api_trips')