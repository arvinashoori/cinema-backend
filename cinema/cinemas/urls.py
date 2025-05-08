from django.urls import path
from .views import ShowtimeCreateView,ShowTimesListView

urlpatterns = [
    path('showtimes/create',ShowtimeCreateView.as_view(),name='cinema_list'),
    path('showtimes/',ShowTimesListView.as_view(),name='showtime_list'),
]
