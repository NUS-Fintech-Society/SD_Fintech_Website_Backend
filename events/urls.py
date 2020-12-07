from django.urls import path, include
from . import views

urlpatterns = [
  path('events/', views.EventListView.as_view()),
  path('events/<str:id>/', views.EventDetailsView.as_view()),
]