from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import FeePayment
from notifications.services import send_sms_notification

def notify_parent_on_payment(sender, instance, created, **kwargs):
    if created:
        message = f"Dear Parent, we have received KES {instance.amount_paid} for {instance.student.name} on {instance.date_paid}. Thank you for your payment. Download your receipt"
        # Here you would call the function to send the SMS
        # Example: send_sms_notification(instance.parent.phone_number, message)
        send_sms_notification(instance.parent.phone_number, message)
