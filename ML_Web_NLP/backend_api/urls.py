from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'companies', views.companiesViewSet)
router.register(r'headlines', views.headlinesViewSet)

# Wire up our API using automatic URL routi ng.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace = 'rest_framework')),
    path('headlines_scores/<str:company>/<date:start>/<date:end>', views.companyWeeklyScores),
    path('positive_scores/<str:company>/<date:start>/<date:end>', views.companyPositiveScores),
    path('negative_scores/<str:company>/<date:start>/<date:end>', views.companyNegativeScores),
    path('neutral_scores/<str:company>/<date:start>/<date:end>', views.companyNeutralScores),
    path('average_sentiment/<str:company>/<date:start>/<date:end>', views.companyAverageSentiment),
    path('top_positive_news/<str:company>/<date:start>/<date:end>', views.companyPositiveHeadlines),
    path('top_negative_n\ews/<str:company>/<date:start>/<date:end>', views.companyNegativeHeadlines),
]

#A router works with a viewset to route requests. It points to the viewset.