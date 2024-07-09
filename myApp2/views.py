import datetime
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def offset_increase(request,offset):
    return HttpResponse("After "+str(offset)+" increase time is "+str(datetime.datetime.now()+datetime.timedelta(hours=offset)))

def offset_decrease(request,offset):
    return HttpResponse("Before "+str(offset)+" decrement time is "+str(datetime.datetime.now()-datetime.timedelta(hours=offset)))
