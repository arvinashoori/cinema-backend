# cinemas/views.py
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAdminUser
from .models import Showtime
from cinemas.serializers import ShowtimeSerializer

class ShowtimeCreateView(generics.CreateAPIView):
    queryset = Showtime.objects.all()
    serializer_class = ShowtimeSerializer
    permission_classes = [IsAdminUser]

    def perform_create(self, serializer):
        serializer.save()

class ShowTimesListView(generics.ListAPIView):
    queryset = Showtime.objects.all()
    serializer_class = ShowtimeSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return Showtime.objects.select_related('movie', 'theater__Cinema').prefetch_related('theater__seats')

class ShowtimeDetailView(generics.RetrieveAPIView):
    queryset = Showtime.objects.all()
    serializer_class = ShowtimeSerializer
    permission_classes = [AllowAny]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['show_available_only'] = self.request.query_params.get('available_only', 'false').lower() == 'true'
        return context

    def get_queryset(self):
        return Showtime.objects.select_related('movie', 'theater__Cinema').prefetch_related('theater__seats')