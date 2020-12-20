from django.urls import path

from . import views

urlpatterns = [
    path('departments', views.index, name='index'),
]