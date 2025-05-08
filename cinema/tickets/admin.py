from django.contrib import admin
from tickets.models import Ticket

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ['user', 'showtime', 'seat_number', 'purchase_time']
    list_filter = ['purchase_time']
    search_fields = ['user__username', 'showtime__movie__title', 'seat_number']