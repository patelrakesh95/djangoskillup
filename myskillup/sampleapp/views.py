from django.shortcuts import render
from  django.http import request,HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Hello World!")

def renderIndex(request):
    return render(request,'sampleapp/index.html',None)
