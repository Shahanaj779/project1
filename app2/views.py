from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def first(request):
    return HttpResponse('<h1> Nandha is a Good boy</h1>')


def second(request):
    return HttpResponse('<h1> Nandha is Glamours Boy</h1>')