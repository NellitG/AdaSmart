from django.urls import path
from . import views

urlpatterns = [
    path('remind-debt/', views.send_debt_reminders, name='send_debt_reminders'),
]