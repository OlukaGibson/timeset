from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def time(request):
    return HttpResponse('Hello, Gibson!')