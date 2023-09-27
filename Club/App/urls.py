from django.contrib import admin
from django.urls import path, include
from App.views import main, main_page, news,team

urlpatterns = [
    path('main',main, name='main'),
    path('main_page',main_page, name='main_page'),
    path('news',news, name='news'),
    path('team',team, name='team'),
]
