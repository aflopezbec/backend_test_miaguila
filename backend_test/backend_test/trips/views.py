from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from backend_test.trips.serializers import TripSerializer

from backend_test.trips.models import Trip


class TripView( ListAPIView ):
    """
    Endpoint to see the trips list
    ---
    parameters:
    - name: limit
      description: count of trips by page
      required: false
      paramType: Integer
    - name: offset
      description: number the initial element
      required: false
      paramType: Integer
    """
    serializer_class = TripSerializer
    queryset = Trip.objects.all()


# Create your views here.
@api_view(["GET"])
def countTrips(request):
    """
    Endpoint to know the trip count
    ---
    parameters:
    - name: city
      description: name of the city by filter
      required: false
      paramType: String
    - name: country
      description: name of the country by filter
      required: false
      paramType: String
    """
    count_trips = None
    if (request.query_params.get('city')):
        print(request.query_params.get('city'))
        count_trips = Trip.objects(city__name=request.query_params.get('city')).count()
    elif (request.query_params.get('country')):
        print(request.query_params.get('country'))
        count_trips = Trip.objects(country__name=request.query_params.get('country')).count()
    else:
        count_trips = Trip.objects.all().count()
    return Response(
        data = {
            'count_trips': count_trips
        }
    )


