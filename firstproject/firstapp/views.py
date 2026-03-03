from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
# Create your views here.

def index(request):
    return render(request, "index.html")


def about(request):
    return HttpResponse("<h2>Saber acerca mas de esta app </h2>")

def user(request,name):
    return HttpResponse(f"<h2>Hello, {name}, welcome to the home page of firstapp</h2>")

def book(request, id):
    book=Book.objects.get(id=id)
    context={'book':book}
    return render(request,'book.html',context)
    
def books(request):
    books=Book.objects.all()
    context={'books': books}
    return render(request,'list_books.html',context)

def getbook(request):
    context={}
    return render(request,"bookform.html",context)

def langs(request):
    context={"langs": ["Python","Java","C++"]}
    return render(request,'template.html', context)