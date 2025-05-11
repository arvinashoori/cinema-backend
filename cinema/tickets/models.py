
from django.db import models
from users.models import CustomUser
from cinemas.models import Showtime, Seat

class Ticket(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    showtime = models.ForeignKey(Showtime, on_delete=models.CASCADE, related_name="tickets")
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE, related_name="tickets")
    purchase_time = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):        
        self.seat.is_reserved = True
        self.seat.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"بلیط {self.showtime} - {self.seat.seat_number}"