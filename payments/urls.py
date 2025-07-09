from django.urls import path
from . import views

urlpatterns = [
   path('test-payment/', views.test_payment_entry, name='test_payment'), 
]