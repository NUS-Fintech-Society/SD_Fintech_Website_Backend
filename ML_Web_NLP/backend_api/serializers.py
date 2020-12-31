#serializers.py 

from rest_framework import serializers
from .models import companies
from .models import headlines

class companiesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = companies
        fields = ('id', 'company_name')

class headlinesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = headlines
        fields = ('id', 'company_name', 'title', 'date_posted', 'week', 'year', 'score')