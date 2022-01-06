from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello Word")

def features(request):
    return HttpResponse("Feature Page")

def about(request):
    return HttpResponse("About Page")

def contact(request):
    return HttpResponse("Contact Page")