from django.http import HttpResponse
from django.shortcuts import render


def main(request):
    return HttpResponse('Strona główna')

def main_page(request):
    return render (request,"main_page.html",)

def news(request):
    return render (request,"news.html",)

def team(request):
    return render (request,"team.html",)