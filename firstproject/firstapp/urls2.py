from django.urls import path
from . import views
urlpatterns=[
    #route es la string de URL, excluye host y prefix
    #views.index es la funcion index de views
    #path('/', IndexView.as_view(), name='index'),
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('login/', views.login, name='login'),

]