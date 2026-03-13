from rest_framework import serializers
from .models import Ticket
#ModelSerializer generates the fiels automatically based on the model we specify in the Meta class. It also provides default implementations for create() and update() methods, which can be overridden if needed. By using ModelSerializer, we can save time and effort when creating serializers for our models, as it eliminates the need to manually define each field and its corresponding validation logic.
class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = "__all__"