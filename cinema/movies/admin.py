
from django.contrib import admin
from movies.models import Movie,Genre

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', 'duration', 'poster']
    search_fields = ['title']
    list_filter = ['duration']
    prepopulated_fields = {'description': ('title',)}  # پر کردن خودکار توضیحات (اختیاری)


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']    