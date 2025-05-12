from django.urls import path
from .views import TicketCreateView,TicketCancelView

urlpatterns = [
    path('create/',TicketCreateView.as_view(),name='ticket_create'),
    path('<int:pk>/cancel/', TicketCancelView.as_view(), name='ticket-cancel'),
]
