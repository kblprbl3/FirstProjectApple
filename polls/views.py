from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse
from django.template import loader

def index(request):
    return render(request, 'polls/index.html',)
def about(request):
    return render(request, 'polls/about.html',)
def mac(request):
    return render(request, 'polls/mac.html',)
def ipad(request):
    return render(request, 'polls/ipad.html',)
def iphone(request):
    return render(request, 'polls/iphone.html',)