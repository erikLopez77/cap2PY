from .models import Ticket, TicketSerializer
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.permissions import AllowAny


class TicketListCreateView(generics.ListCreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_class = [AllowAny]

class TicketRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_class = [AllowAny]

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'tickets': reverse('ticketlist',
        request=request, format=format),
        'ticket-detail': reverse('ticketdetail',
        args=[1], request=request, format=format),
    })