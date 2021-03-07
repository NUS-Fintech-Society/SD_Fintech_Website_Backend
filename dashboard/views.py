from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import datetime
import json
import numpy as np

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
        print(data)
        output = []
        weekly_scores = {}
        for row in data:
            week = str(row["week"])
            if len(week) == 1:
                week = "0" + week
            year_week = str(row['year']) + "_" + week
            if year_week not in weekly_scores:
                weekly_scores[year_week] = [0,0,0,[]]
                if row['score'] > 0.0005:
                    weekly_scores[year_week][0]+=1
                elif row['score'] < -0.0005:
                    weekly_scores[year_week][1] +=1
                else:
                    weekly_scores[year_week][2]+=1
                weekly_scores[year_week][3].append(row['score'])
            else:
                if row['score'] > 0.0005:
                    weekly_scores[year_week][0]+=1
                elif row['score'] < -0.0005:
                    weekly_scores[year_week][1] +=1
                else:
                    weekly_scores[year_week][2]+=1
                weekly_scores[year_week][3].append(row['score'])

        final_weekly_scores = []
        for weeks in weekly_scores:
            temp_dict = {}
            temp_dict["Year_Week"] = weeks
            temp_dict["positive"] = weekly_scores[weeks][0]
            temp_dict["negative"] = weekly_scores[weeks][1]
            temp_dict["neutral"] = weekly_scores[weeks][2]
            if len(weekly_scores[weeks][3]) == 0:
                temp_dict["score"] = 0
            else:  
                temp_dict["score"] = np.mean(weekly_scores[weeks][3])
            final_weekly_scores.append(temp_dict)
        return JsonResponse(list(final_weekly_scores), safe = False)
    
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
            if row['score'] > 0.0005 :
                positive_scores += 1
            total_scores += 1
        if total_scores == 0:
            final_score = 0
        else:
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
        if total_scores == 0:
            final_score = 0
        else:
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
            total_scores+=1
        if total_scores == 0:
            final_score = 0
        else:
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
        if total_count == 0:
            final_score = 0
        else:
            final_score = round(total_scores/total_count, 3)
    return JsonResponse(final_score, safe = False)

def companyPositiveHeadlines(request, company, start, end):
    if request.method == 'GET':
        data = headlines.objects.filter(company_name=company).filter(date_posted__gte = start).filter(date_posted__lte = end).filter(score__gte = 0.000001).order_by('score').values()[:5]
        mostPositiveNews = []
        counter = 1
        for row in data:
            print(row)
            #mostPositiveNews.append(row['title'])
            title = row['title']
            company = row['company_name_id']
            id = counter
            counter+=1
            mostPositiveNews.append({'id':id, "commpany":company, "title": title})
    return JsonResponse(list(mostPositiveNews), safe = False)
            
def companyNegativeHeadlines(request, company, start, end):
    if request.method == 'GET':
        data = headlines.objects.filter(company_name=company).filter(date_posted__gte = start).filter(date_posted__lte = end).filter(score__lte = -0.000001).order_by('score').values()[:5]
        mostNegativeNews = []
        counter= 0
        for row in data:
            print(row)
            #mostPositiveNews.append(row['title'])
            title = row['title']
            company = row['company_name_id']
            id = counter
            counter+=1
            mostNegativeNews.append({'id':id, "commpany":company, "title": title})
    return JsonResponse(list(mostNegativeNews), safe = False)
 
def getCompanies(request):
    if request.method == 'GET':
        data =[]
        for i in companies.objects.values():
            data.append(i['company_name'])
        return JsonResponse(list(data), safe=False)