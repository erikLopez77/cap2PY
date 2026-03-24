from django.db import models
from rest_framework import serializers

class Ticket(models.Model):
    flight_number = models.CharField(max_length=10)
    passenger_name = models.CharField(max_length=100)
    departure_time = models.DateTimeField()
    seat_number = models.CharField(max_length=5)

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = "__all__"