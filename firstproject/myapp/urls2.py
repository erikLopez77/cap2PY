from django.urls import path
from . import views
urlpatterns=[
    #route es la string de URL, excluye host y prefix
    #views.index es la funcion index de views
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('login/', views.auth_login, name='login'),
    path('addbook/', views.addbook, name='addbook'),
    path("getbook/<int:id>/", views.getbook,name="getbook"),
    path('books/<int:price>/', views.books, name='booksprice'),
    path('myview/', views.myview, name="myview"),
]