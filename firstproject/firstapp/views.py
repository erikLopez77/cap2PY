from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from .forms import BookForm
from django.views.generic import UpdateView, CreateView, DeleteView,DetailView,ListView
# Create your views here

class BookCreateView(CreateView):
    model = Book
    fields = "__all__"
    template_name = 'book_create_form.html'
    success_url = '../books/'

class BookUpdateView(UpdateView):
    model = Book
    fields = '__all__'
    template_name = "book_create_form.html"
    success_url = "../books/"

class BookDeleteView(DeleteView):
    model = Book
    template_name = "book_confirm_delete.html"
    success_url = "../books/"

    def get_object(self):
        return Book.objects.get(author=self.kwargs['author'])

class BookDetailView(DetailView):
    model = Book
    template_name = "book.html"

    def get_object(self):
        return Book.objects.get(id=self.kwargs['pk'])

class BookListView(ListView):
    model = Book
    template_name = "list_books.html"

    def get_context_data(self, **kwargs):
        books=Book.objects.all()
        context={'books': books}
        return context

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

def getbook(request,author):
    b1=Book.objects.get(author=author)
    form=BookForm(instance=b1)
    context={'form':form}
    return render(request,"bookform.html",context)

def addbook(request):
    if request.method =="POST":
        form=BookForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("<h2>Book added successfully</h2>")

def langs(request):
    context={"langs": ["Python","Java","C++"]}
    return render(request,'template.html', context)

def aboutbooks(request):
    books=Book.objects.all()
    context={'books': books}
    return render(request,'aboutbooks.html',context)