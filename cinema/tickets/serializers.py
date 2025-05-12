# tickets/serializers.py
from rest_framework import serializers
from tickets.models import Ticket
from cinemas.models import Seat,Showtime
from cinemas.serializers import ShowtimeSerializer

class TicketSerializer(serializers.ModelSerializer):
    showtime = serializers.PrimaryKeyRelatedField(queryset=Showtime.objects.all())
    seat = serializers.PrimaryKeyRelatedField(queryset=Seat.objects.all(), allow_null=True)
    seat_number = serializers.CharField(source='seat.seat_number', read_only=True) 

    class Meta:
        model = Ticket
        fields = ['id', 'user', 'showtime', 'seat', 'seat_number', 'purchase_time']
        extra_kwargs = {'user': {'read_only': True}}

    def validate_seat(self, value):
        if value and value.is_reserved:
            raise serializers.ValidationError("این صندلی قبلاً رزروشده است.")
        return value

def create(self, validated_data):
    if 'showtime' not in validated_data or validated_data['showtime'] is None:
        raise serializers.ValidationError({"showtime": "مقدار showtime اجباری است و نمی‌تواند خالی باشد."})
    validated_data['user'] = self.context['request'].user
    return super().create(validated_data)