from django.urls import path, include
from . import views

urlpatterns = [
  path('contact/', views.ContactFormListView.as_view()),
  path('contact/<str:id>/', views.ContactFormDetailsView.as_view()),
]