from django.contrib import admin
from cinemas.models import Cinema, Theater, Showtime, Seat

@admin.register(Cinema)
class CinemaAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'phone']
    search_fields = ['name', 'address', 'phone']

@admin.register(Theater)
class TheaterAdmin(admin.ModelAdmin):
    list_display = ['get_cinema_name', 'name', 'total_seats']
    search_fields = ['name', 'cinema__name']
    #list_filter = ['cinema']

    def get_cinema_name(self, obj): 
        return obj.Cinema.name if obj.Cinema else "بدون سینما"

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

        current_seat_count = obj.seats.count()
        if obj.total_seats > current_seat_count:

            for i in range(current_seat_count + 1, obj.total_seats + 1):
                seat_number = f"A{i}" 
                Seat.objects.get_or_create(theater=obj, seat_number=seat_number, defaults={'is_reserved': False})
        elif obj.total_seats < current_seat_count:
            seats_to_delete = obj.seats.all()[obj.total_seats:]
            for seat in seats_to_delete:
                seat.delete()

@admin.register(Showtime)
class ShowtimeAdmin(admin.ModelAdmin):
    list_display = ['movie', 'theater', 'start_time', 'price']
    list_filter = ['theater', 'start_time']
    search_fields = ['movie__title', 'theater__name']
    autocomplete_fields = ['movie', 'theater']

@admin.register(Seat)
class SeatAdmin(admin.ModelAdmin):
    list_display = ['theater', 'seat_number', 'is_reserved']
    list_filter = ['is_reserved', 'theater']
    search_fields = ['seat_number', 'theater__name']
    autocomplete_fields = ['theater']