from django.shortcuts import render
from django.http import HttpResponse

def hello_world(requests: HttpResponse):
    return HttpResponse('Hello, World')
# Create your views here.
