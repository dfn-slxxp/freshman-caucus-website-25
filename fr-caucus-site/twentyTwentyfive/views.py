from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def home(request):
    template = loader.get_template('twentyTwentyFive/home.html')
    return HttpResponse(template.render())

def cabinet(request):
    template = loader.get_template('twentyTwentyFive/cabinet.html')
    return HttpResponse(template.render())

def events(request):
    template = loader.get_template('twentyTwentyFive/events.html')
    return HttpResponse(template.render())
