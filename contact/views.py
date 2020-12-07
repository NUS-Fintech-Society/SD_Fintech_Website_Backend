from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status

# Create your views here.
from .serializers import ContactFormSerializer
from .models import ContactForm

class ContactFormListView(APIView):

  def get(self, request):
      forms = ContactForm.objects.all()
      serializer = ContactFormSerializer(forms, many=True)
      return Response(serializer.data)

  def post(self, request):
      serializer = ContactFormSerializer(data=request.data)

      if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  

class ContactFormDetailsView(APIView):

  def get_object(self, id):
    try:
      return ContactForm.objects.get(id=id)
    except ContactForm.DoesNotExist:
      return Response(status=status.HTTP_404_NOT_FOUND)

  def get(self, request, id):
    form = self.get_object(id)
    serializer = ContactFormSerializer(form)
    return Response(serializer.data)
