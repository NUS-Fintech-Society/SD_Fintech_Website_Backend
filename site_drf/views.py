from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List, Create Contact Form Submissions': '/contact/',
        'View Contact Form Submission Details': '/contact/<id>/',
        'List, Create Events':'/events/',
        'View Event Details':'/events/<id>/',
        'List, Projects done by the Society': '/projects/',
        'View Project Details': '/projects/<id>/',
        'List, Projects done by a specific department': '/projects/department/<deptId>/',
        'View, all Departments': '/departments/',
        'View, Department Details': '/departments/<id>/',
        'View Dashboard Average Sentiment Score':'/headlines_scores/<company>/<start>/<end>',
        'View Dashboard Average Sentiment':'/average_sentiment/<company>/<start>/<end>',
        'View Dashboard Positive News Proportion':'/positive_scores/<company>/<start>/<end>',
        'View Dashboard Negative News Proportion':'/negative_scores/<company>/<start>/<end>',
        'View Dashboard Neutral News Proportion':'/neutral_scores/<company>/<start>/<end>',
        'View Dashboard Top Positive News':'/top_positive_news/<company>/<start>/<end>',
        'View Dashboard Top Negative News':'/top_negative_news/<company>/<start>/<end>',
        'View Dashboard Companies':'/get_companies',
    }

    return Response(api_urls)
