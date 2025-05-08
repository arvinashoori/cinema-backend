from rest_framework import serializers
from .models import Cinema,Showtime,Theater
from movies.serializers import MovieSerializer

class CinemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cinema
        fields = ['id','name','address','phone']

class TheatorSerializer(serializers.ModelSerializer):
     cinema = CinemaSerializer

     class Meta:
         model= Theater
         fields = ['id','cinema','name','total_seats']

class ShowTimeSerializer(serializers.ModelSerializer):
    movie = MovieSerializer(read_only=True)
    theater = TheatorSerializer(read_only=True)

    class Meta:
        model = Showtime
        fields = ['id','movie','cinema','start_time','price']       