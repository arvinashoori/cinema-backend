from django.contrib import admin
from reviews.models import Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['user', 'movie', 'rating', 'created_at']
    list_filter = ['rating', 'created_at']
    search_fields = ['user__username', 'movie__title', 'comment']