from django.shortcuts import render
from django.http import HttpResponse
import json

# Create your views here.
def funhello(request):
    return HttpResponse("<h1>Welcome to axis Bank</h1>")

def funlogin(request):
    return HttpResponse("<h3>Please login to your account. </h3>")
    


