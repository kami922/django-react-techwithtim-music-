from django.shortcuts import render,HttpResponse

# Create your views here.
def index(requ):
    return HttpResponse("Hello")

def hello(requ):
    return HttpResponse("sec function for git branches")