# cinemas/admin.py
from django.contrib import admin
from cinemas.models import Cinema, Theater, Showtime

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
    get_cinema_name.short_description = 'سینما'


@admin.register(Showtime)
class ShowtimeAdmin(admin.ModelAdmin):
    list_display = ['movie', 'theater', 'start_time', 'price']
    #list_filter = ['theater', 'start_time']  # فعلاً کامنت شده
    search_fields = ['movie__title', 'theater__name']
    autocomplete_fields = ['movie', 'theater']  # برای جستجوی بهتر

    def get_movie_title(self, obj):
        return obj.movie.title if obj.movie else "بدون فیلم"
    get_movie_title.short_description = 'فیلم'

    def get_theater_name(self, obj):
        return obj.theater.name if obj.theater else "بدون سالن"
    get_theater_name.short_description = 'سالن'