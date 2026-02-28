from django.urls import path
from . import views

urlpatterns = [
    #route es la string de URL, excluye host y prefix
    #views.index es la funcion index de views
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path("user/<name>/",views.user,name="user")#default str:
]