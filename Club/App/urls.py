from django.contrib import admin
from django.urls import path, include
from App.views import main, main_page

urlpatterns = [
    path('main',main, name='main'),
    path('main_page',main_page, name='main_page'),
]
