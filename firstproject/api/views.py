from ninja import NinjaAPI
from typing import List
from api.schemas import TicketSchema
from myapi.models import Ticket

api = NinjaAPI()
@api.get("/hello/")
def test(request):
    return {'message': 'Hello World!'}

@api.get("/tickets/", response=List[TicketSchema])
def tickets(request):
    return Ticket.objects.all()

@api.post("/tickets", response={201: TicketSchema})
def create_ticket(request, ticket: TicketSchema):
    Ticket.objects.create(**ticket.dict())
    return ticket