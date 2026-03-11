from urllib import request

from django.shortcuts import render,redirect
# Create your views here.
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import col
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def auth_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username,password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login successful. Hello {}".format(user))
            return redirect('home')
        else:
            messages.error(request, ("There Was An Error Logging In, Try Again..."))
            return redirect('login')
    else:
        return render(request, 'login.html', {})

def logout_user(request):
    logout(request)
    messages.info(request, "You Were Logged Out!")
    return redirect('index')
#we have to create UserCreationForm class
""" 
def register_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,
            password=password)
            login(request, user)
            messages.success(request, ("Registration Successful!"))
            return redirect('index')  
    else:
        return render(request, 'register.html', {}) """
def addbook(request):
    if request.method=="POST":
        data = request.POST
        title = data["title"]
        author = data["author"]
        price = data["price"]
        publisher = data["publisher"]
        doc = Book(title = title, author = author, price =
        price, publisher = publisher)
        doc.save()
        return HttpResponse("Document Successfully Added")
    else:
        return render(request, "book.html", {})

    
def books(request, price):
    books = col.find({"price": {"$gt": price}})
    lst=""
    for book in books:
        lst+="<h2>Title: {} \t Author: {} \t Price: {}</h2>".format(book['title'], book['author'], book['price'])
    print(lst)
    if not lst:
        return HttpResponse("No se encontraron libros con precio mayor a {}".format(price))
    return HttpResponse(lst)

def getbook(request, id):
    book = col.find_one({"id":id})
    return HttpResponse("<h2>Title: {} \t Author: {} \tPrice: {}</h2>".format(book['title'], book['author'],
    book['price']))

@login_required(login_url="../login/")
def myview(request):
    return HttpResponse("This message will be displayed only if a user is logged in")