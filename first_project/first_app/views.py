from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Hello bitches")

def help(request):
    helpdict = {'help_insert':'HELP PAGE'}
    return render(request,'first_app/help.html',context=helpdict)
