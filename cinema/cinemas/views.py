
from rest_framework import generics
from rest_framework.permissions import AllowAny,IsAdminUser
from .models import Showtime
from cinemas.serializers import CinemaSerializer,ShowTimeSerializer

class ShowtimeCreateView(generics.ListAPIView):
    queryset= Showtime.objects.all()
    serializer_class = ShowTimeSerializer
    permission_classes = [IsAdminUser]

    def perform_create(self,serializer):
        serializer.save()

class ShowTimesListView(generics.ListAPIView):
    queryset = Showtime.objects.all()
    serializer_class = ShowTimeSerializer
    permission_classes = [AllowAny]    