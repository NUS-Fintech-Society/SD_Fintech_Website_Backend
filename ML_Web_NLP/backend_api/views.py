from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import datetime
import json

# Create your views here.
from rest_framework import viewsets
from .serializers import companiesSerializer
from .serializers import headlinesSerializer
from .models import companies
from .models import headlines
from django.core import serializers


class companiesViewSet(viewsets.ModelViewSet):
    queryset = companies.objects.all().order_by('company_name')
    serializer_class = companiesSerializer #Helps to convert to JSON format from django formatting

class headlinesViewSet(viewsets.ModelViewSet):
    queryset = headlines.objects.all().order_by('title')
    serializer_class = headlinesSerializer

def companyWeeklyScores(request, company, start, end):
    if request.method == 'GET':
        #data = headlines.objects.raw('SELECT * FROM headlines WHERE company_name = %s AND date_posted >= %s AND date_posted <= %s', [company, start, end])
        #data = headlines.objects.raw('SELECT * FROM headlines WHERE company_name = %s', [company])
        data = headlines.objects.filter(company_name=company).filter(date_posted__gte = start).filter(date_posted__lte = end).values()
        agg_score = [0]*52
        num_score = [0]*52
        for row in data:
            agg_score[row['week'] - 1] += row['score']
            num_score[row['week'] - 1] += 1
        output = []
        for i in range(len(agg_score)):
            if num_score[i] != 0:
                output.append(agg_score[i]/num_score[i])
            else:
                output.append(None)
        return JsonResponse(list(output), safe = False)
    
        #data = serializers.serialize('json', YourModel.objects.raw(query), fields=('id', 'name', 'parent'))
        #print("iodfjofisjf[doi")
        #return data
        #Person.objects.raw('SELECT * FROM myapp_person WHERE last_name = %s', [lname])

def companyPositiveScores(request, company, start, end):
    if request.method == 'GET':
        data = headlines.objects.filter(company_name=company).filter(date_posted__gte = start).filter(date_posted__lte = end).values()
        total_scores = 0
        positive_scores = 0
        for row in data:
            if row['score'] > 0.0005:
                positive_scores += 1
            total_scores += 1
        final_score = round(positive_scores/total_scores, 3)
    return JsonResponse(final_score, safe = False)

def companyNeutralScores(request, company, start, end):
    if request.method == 'GET':
        data = headlines.objects.filter(company_name=company).filter(date_posted__gte = start).filter(date_posted__lte = end).values()
        total_scores = 0
        neutral_scores = 0
        for row in data:
            if (row['score'] < 0.0005) & (row['score'] > -0.0005):
                neutral_scores += 1
            total_scores += 1
        final_score = round(neutral_scores/total_scores, 3)
    return JsonResponse(final_score, safe = False)

def companyNegativeScores(request, company, start, end):
    if request.method == 'GET':
        data = headlines.objects.filter(company_name=company).filter(date_posted__gte = start).filter(date_posted__lte = end).values()
        total_scores = 0
        negative_scores = 0
        for row in data:
            if row['score'] < -0.0005:
                negative_scores += 1
            total_scores += 1
        final_score = round(negative_scores/total_scores, 3)
    return JsonResponse(final_score, safe = False)

def companyAverageSentiment(request, company, start, end):
    if request.method == 'GET':
        data = headlines.objects.filter(company_name=company).filter(date_posted__gte = start).filter(date_posted__lte = end).values()
        total_scores = 0
        total_count = 0
        for row in data:
            total_scores += row['score']
            total_count += 1
        final_score = round(total_scores/total_count, 3)
    return JsonResponse(final_score, safe = False)

def companyPositiveHeadlines(request, company, start, end):
    if request.method == 'GET':
        data = headlines.objects.filter(company_name=company).filter(date_posted__gte = start).filter(date_posted__lte = end).filter(score__gte = 0.000001).order_by('score').values()[:5]
        mostPositiveNews = []
        for row in data:
            mostPositiveNews.append(row['title'])
    return JsonResponse(list(mostPositiveNews), safe = False)
            
def companyNegativeHeadlines(request, company, start, end):
    if request.method == 'GET':
        data = headlines.objects.filter(company_name=company).filter(date_posted__gte = start).filter(date_posted__lte = end).filter(score__lte = -0.000001).order_by('score').values()[:5]
        mostNegativeNews = []
        for row in data:
            mostNegativeNews.append(row['title'])
    return JsonResponse(list(mostNegativeNews), safe = False)
 
