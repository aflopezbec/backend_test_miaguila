from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework_mongoengine.viewsets import ModelViewSet
from backend_test.trips.serializers import TripSerializer

from backend_test.trips.models import Trip


class TripView( ModelViewSet ):
    """
    Endpoint to see the trips list
    ---
    parameters:
    - name: limit
      description: count of trips by page
      required: false
      paramType: Integer
    - name: offset
      description: number the initial element in page
      required: false
      paramType: Integer
    - name: fields
      description: list of fields to show separate by ,
      required: false
      paramType: Integer
    - name: status
      description: status of trip
      required: false
      paramType: String
      choices: ['onWay','near','started']
    """
    lookup_field = 'id'
    serializer_class = TripSerializer
    queryset = Trip.objects.all()
    http_method_names = ['get', 'post', 'put']

    def list(self, request, **kwargs):
        """
        This view should return a list of all the trips
        with a status selected.
        """
        queryset = None  
        if (self.request.query_params.get('status')):
            queryset =  Trip.objects(status=self.request.query_params.get('status'))
        else:
            queryset = Trip.objects.all()
        queryset = self.filter_queryset(queryset)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

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

def handler404(request, exception):
    return JsonResponse({'Message':'Page not found', 'status': status.HTTP_404_NOT_FOUND}, status=404)