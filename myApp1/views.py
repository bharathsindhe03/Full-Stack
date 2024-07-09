from django.http import HttpResponse
from django.shortcuts import render
import datetime

def current_time(request):
    return HttpResponse("the current time = "+str(datetime.datetime.now()))
