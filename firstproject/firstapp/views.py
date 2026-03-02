from django.shortcuts import render
from django.http import HttpResponse
import sqlite3
# Create your views here.

def index(request):
    return render(request, "index.html")


def about(request):
    return HttpResponse("<h2>Saber acerca mas de esta app </h2>")

def user(request,name):
    return HttpResponse(f"<h2>Hello, {name}, welcome to the home page of firstapp</h2>")

def books(request):
    conn= sqlite3.connect("db.sqlite3")
    cur=conn.cursor()
    qry="   SELECT * FROM Books"
    cur.execute(qry)
    books=cur.fetchall()
    return HttpResponse(str(books))

def book(request, id):
    conn= sqlite3.connect("db.sqlite3")
    cur=conn.cursor()
    qry="   SELECT * FROM Books WHERE id=?"
    cur.execute(qry,(id,))
    book=cur.fetchone()
    return HttpResponse(str(book))