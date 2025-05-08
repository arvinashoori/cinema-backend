from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import Movie
from .serializers import MovieSerializer

class MovieListView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [AllowAny]
