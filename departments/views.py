from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status

# Create your views here.
from .serializers import DepartmentSerializer
from .models import Department

class DepartmentListView(APIView):

    def get(self, request):
        departments = Department.objects.all()
        serializer = DepartmentSerializer(departments, many=True)
        return Response(serializer.data)


#def index(request):
 #   return HttpResponse("Departments page here")