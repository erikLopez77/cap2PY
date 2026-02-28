from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, "index.html")


def about(request):
    return HttpResponse("<h2>Saber acerca mas de esta app </h2>")

def user(request,name):
    return HttpResponse(f"<h2>Hello, {name}, welcome to the home page of firstapp</h2>")