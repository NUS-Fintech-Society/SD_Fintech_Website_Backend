from django.urls import path

from . import views

urlpatterns = [
    path('departments/', views.DepartmentListView.as_view()),
    path('departments/<str:id>/', views.DepartmentDetailsView.as_view())
]