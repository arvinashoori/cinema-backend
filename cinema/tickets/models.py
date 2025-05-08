from django.db import models
from users.models import CustomUser
from cinemas.models import Showtime

class Ticket(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name="tickets")
    showtime = models.ForeignKey(Showtime,on_delete=models.CASCADE,related_name="tickets")
    seat_number = models.CharField(max_length=10)
    purchase_time = models.DateTimeField(auto_now_add=True)
    is_canceled = models.BooleanField(default=False)

    class Meta:
        unique_together = ('showtime','seat_number')

    def __str__(self):
        return f"بلیط {self.showtime} - صندلی {self.seat_number}"
    
        