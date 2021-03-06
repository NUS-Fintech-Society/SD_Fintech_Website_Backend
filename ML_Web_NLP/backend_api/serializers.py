#serializers.py 

from rest_framework import serializers
from .models import companies
from .models import headlines

class companiesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = companies
        #fields = ('company_name')
        fields = '__all__'

class headlinesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = headlines
        #fields = ('id', 'company_name_id', 'title', 'date_posted', 'week', 'year', 'score')
        fields = '__all__'