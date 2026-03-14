from django.urls import path
from . import views

urlpatterns = [
    path('hello/',views.sayHello,name="hello"),
    path('drf/', views.drfRoute, name='drf'),
    path('', views.api_root, name='api-root'),
    path('tickets/', views.ticket_list, name='ticket-list'),
    path('ticket/<int:pk>/', views.ticket_detail, name='ticket-detail'),
]