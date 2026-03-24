from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_root, name='api-root'),
    path('tickets/', views.TicketListCreateView.as_view(), name='ticketlist'),
    path('tickets/<int:pk>/', views.TicketRetrieveUpdateDeleteView.as_view(), name='ticketdetail'),
]