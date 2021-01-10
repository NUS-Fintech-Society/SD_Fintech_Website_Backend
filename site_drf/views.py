from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List, Create Contact Form Submissions': '/contact/',
        'View Contact Form Submission Details': '/contact/<id>/',
        'List, Projects done by the Society': '/projects/',
        'View Project Details': '/projects/<id>/',
        'List, Projects done by a specific department': '/projects/department/<deptId>/',
        'View, all Deparments': '/departments/',
        'View, Department Details': '/departments/<id>/',
    }

    return Response(api_urls)
