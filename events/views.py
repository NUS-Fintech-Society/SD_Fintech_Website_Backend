from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status

# Create your views here.
from .serializers import EventSerializer
from .models import Event

class EventListView(APIView):

  def get(self, request):
      events = Event.objects.all()
      serializer = EventSerializer(events, many=True)
      return Response(serializer.data)

  def post(self, request):
      serializer = EventSerializer(data=request.data)

      if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  

class EventDetailsView(APIView):

  def get_object(self, id):
    try:
      return Event.objects.get(id=id)
    except Event.DoesNotExist:
      return Response(status=status.HTTP_404_NOT_FOUND)

  def get(self, request, id):
    event = self.get_object(id)
    serializer = EventSerializer(event)
    return Response(serializer.data)
