from rest_framework import serializers
from .models import Ticket
from cinemas.models import Showtime

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['id','showtime','seat_number','purchase_time']
        read_only_fields = ['purchase_time']

        def validate(self,data):
            showtime = data['showtime']
            seat_number = data['seat_number']
            if Ticket.objects.filter(showtime=showtime,seat_number=seat_number).exists():
                raise serializers.ValidationError('این صندلی قبلا رزرو شده')
            return data