from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics,status
from rest_framework.permissions import IsAuthenticated,AllowAny
from . models import Ticket
from . serializers import TicketSerializer

class TicketCreateView(generics.CreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
    
class TicketCancelView(generics.DestroyAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.user != request.user and not request.user.is_staff:
            raise PermissionDenied("شما اجازه لغو این بلیط را ندارید.")
        
        if instance.seat:
            instance.seat.is_reserved = False
            instance.seat.save()

        self.perform_destroy(instance)
        return Response({"message": "بلیط با موفقیت لغو شد."}, status=status.HTTP_200_OK)

    def perform_destroy(self, instance):
        instance.delete()    