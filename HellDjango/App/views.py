from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def hello(request):
   return HttpResponse("hello")


def hehe(request):
   return HttpResponse("呵呵")

def haha(request):
   return HttpResponse("<h1>hello</h1>")


def index(request):
   return render(request,"index.html")

def home(request):
   return render(request,"home.html")