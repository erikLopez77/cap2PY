from django.urls import include, path
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('tickets', views.TicketViewSet)

urlpatterns = [
    path('hello/',views.sayHello,name="hello"),
    path('drf/', views.drfRoute, name='drf'),
    path('', include('rest_framework.urls')),
    #path('tickets/', views.ticket_list, name='ticket-list'),
    #path('ticket/<int:pk>/', views.ticket_detail, name='ticket-detail'),
    #class-based views
    path('tickets/', views.TicketViewSet.as_view({
        'get':'list','post':'create'
    }),name='ticket-list'),
    path('ticket/<int:pk>/', views.TicketViewSet.as_view({
        'get':'retrieve','put':'update','delete':'destroy'
    }),name='ticket-detail'),
    path("",include(router.urls)),
    path('secured/', views.auhtenticated_view,name='secured'),
    path('api-token',obtain_auth_token),
]