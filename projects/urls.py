from django.urls import path, include
from . import views

urlpatterns = [
    path('projects/', views.ProjectListView.as_view()),
    path('projects/<str:id>/', views.ProjectDetailsView.as_view()),
]
