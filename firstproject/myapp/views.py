from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from .models import col

def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def login(request):
    return render(request, "login.html")

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