from django.contrib import admin
from django.urls import path, include
from App.views import main

urlpatterns = [
    path('main',main, name='main'),
]
