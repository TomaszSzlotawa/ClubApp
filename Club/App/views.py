from django.http import HttpResponse
from django.shortcuts import render


def main(request):
    return HttpResponse('Strona główna')

def main_page(request):
    return render (request,"main.html",)