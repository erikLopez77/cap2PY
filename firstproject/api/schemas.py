from datetime import datetime
from ninja import Schema

class TicketSchema(Schema):
    flight_number : str
    passenger_name : str
    departure_time : datetime
    seat_number : str