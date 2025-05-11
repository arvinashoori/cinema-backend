from django.contrib import admin
from tickets.models import Ticket

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ['user', 'showtime', 'get_seat_number', 'purchase_time']
    list_filter = ['purchase_time']
    search_fields = ['user__username', 'showtime__movie__title', 'seat__seat_number']
    autocomplete_fields = ['showtime', 'seat'] 
    def get_seat_number(self, obj):
        return obj.seat.seat_number if obj.seat else "بدون صندلی"
    get_seat_number.short_description = 'شماره صندلی'

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.select_related('seat', 'showtime')  