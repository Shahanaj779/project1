from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def first(request):
    return HttpResponse('<h1>Hiiii......World<h1>')


def second(request):
    return HttpResponse('<h1><marquee>Goood......Morning </marquee></h1>')
