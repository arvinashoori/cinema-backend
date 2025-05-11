from django.urls import path
from .views import ShowtimeCreateView,ShowTimesListView,ShowtimeDetailView

urlpatterns = [
    path('showtimes/create',ShowtimeCreateView.as_view(),name='cinema_list'),
    path('showtimes/',ShowTimesListView.as_view(),name='showtime_list'),
    path('showtimes/<int:pk>/', ShowtimeDetailView.as_view(), name='showtime-detail'),
]
