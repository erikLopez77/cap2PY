from django.urls import path
from . import views
from .myview import MyView
from .indexView import IndexView
from firstapp.views import BookCreateView, BookUpdateView, BookDeleteView, BookDetailView, BookListView
urlpatterns = [
    #route es la string de URL, excluye host y prefix
    #views.index es la funcion index de views
    #path('/', IndexView.as_view(), name='index'),
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('login/', views.about, name='login'),
    path("user/<name>/",views.user,name="user"),#default str:
    path("book/<int:id>/",views.book,name="book"),
    path("books/",views.books,name="books"),
    path("getbook/<author>",views.getbook,name="getbook"),
    path("addbook",views.addbook,name="addbook"),
    #path("list/",views.langs,name="langs"),
    path("name/",MyView.as_view(),name="name"),

    path("newbook/", BookCreateView.as_view(),name="newbook"),
    path("update/<int:pk>", BookUpdateView.as_view(), name="update"),
    path("delete/<author>", BookDeleteView.as_view(), name="delete"),
    path("show/<int:pk>", BookDetailView.as_view(), name="show"),
    path("list/", BookListView.as_view(), name="list"),
    path("aboutbooks/",views.aboutbooks,name="aboutbooks"),
]


