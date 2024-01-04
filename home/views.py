from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Hey I am a django server.</h1>")


def successPage(request):
    return HttpResponse("<h2>Hey this is a success page.</h2>")