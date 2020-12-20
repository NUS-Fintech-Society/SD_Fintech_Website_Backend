from django.urls import path

from . import views

urlpatterns = [
    path('departments/', views.DepartmentListView.as_view())
]