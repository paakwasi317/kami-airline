from django.contrib import admin
from django.urls import path
from .views import AirplaneListView


urlpatterns = [
    path('airplane/calculate', AirplaneListView.as_view(), name='airplane'),
]