from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Ticket
from .serializers import TicketSerializer
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

@api_view()
def sayHello(request):
    return Response({"message": "Hello, world!"})

@api_view()
def drfRoute(request):
    return Response({'message': 'REST API designed by Django REST Framework'})

@api_view()
def api_root(request):
    return Response({
        'hello': reverse('hello', request=request),
        'drf': reverse('drf', request=request),
    })

@api_view(['GET', 'POST'])
def ticket_list(request):
    if request.method=='GET':
        tickets = Ticket.objects.all()
        serialized_tickets = TicketSerializer(tickets,
        many=True,context={'request': request})
        return Response(serialized_tickets.data)
    elif request.method=='POST':
        serialized_ticket = TicketSerializer(data=request.data,context={'request': request})
        serialized_ticket.is_valid(raise_exception=True)
        serialized_ticket.save()
        return Response(serialized_ticket.validated_data,status.HTTP_201_CREATED)
    
@api_view(['GET','PUT', 'DELETE'])
def ticket_detail(request, pk):
    ticket = Ticket.objects.get(pk=pk)
    if request.method=='GET':
        serialized_ticket = TicketSerializer(ticket,context={'request':request})
        return Response(serialized_ticket.data)
    elif request.method=='PUT':
        ticket.flight_number = request.data['flight_number']
        ticket.save()
        serialized_ticket=TicketSerializer(ticket,data=request.data,context={'request': request})
        return Response(serialized_ticket.data, status=400)
    elif request.method=='DELETE':
        ticket.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class TicketListView(APIView):
    def get(self, request):
        tickets = Ticket.objects.all()
        serialized_tickets = TicketSerializer(tickets,
        many=True,context={'request': request})
        return Response(serialized_tickets.data)
    def post(self, request):
        serialized_ticket = TicketSerializer(data=request.data,context={'request': request})
        serialized_ticket.is_valid(raise_exception=True)
        serialized_ticket.save()
        return Response(serialized_ticket.validated_data,status.HTTP_201_CREATED)
    
class TicketDetailView(APIView):
    def get(self, request, pk):
        ticket = Ticket.objects.get(pk=pk)
        serialized_ticket = TicketSerializer(ticket,context={'request': request})
        return Response(serialized_ticket.data)
    def put(self, request, pk):
        ticket = Ticket.objects.get(pk=pk)
        ticket.flight_number = request.data['flight_number']
        ticket.save()
        serialized_ticket=TicketSerializer(ticket,data=request.data,context={'request': request})
        return Response(serialized_ticket.data, status=400)
    def delete(self, request, pk):
        ticket = Ticket.objects.get(pk=pk)
        ticket.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)