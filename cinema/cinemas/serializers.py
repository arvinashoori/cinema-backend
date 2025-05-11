# cinemas/serializers.py
from rest_framework import serializers
from cinemas.models import Cinema, Theater, Showtime, Seat
from movies.serializers import MovieSerializer

class CinemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cinema
        fields = ['id', 'name', 'address', 'phone']

class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = ['id', 'seat_number', 'is_reserved']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if self.context.get('show_available_only', False) and representation['is_reserved']:
            return None 
        return representation

class TheaterSerializer(serializers.ModelSerializer):
    cinema = CinemaSerializer(read_only=True)
    seats = SeatSerializer(many=True, read_only=True)

    class Meta:
        model = Theater
        fields = ['id', 'cinema', 'name', 'total_seats', 'seats']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['seats'] = [seat for seat in representation['seats'] if seat is not None]
        return representation

class ShowtimeSerializer(serializers.ModelSerializer):
    movie = MovieSerializer(read_only=True)
    theater = TheaterSerializer(read_only=True)

    class Meta:
        model = Showtime
        fields = ['id', 'movie', 'theater', 'start_time', 'price']