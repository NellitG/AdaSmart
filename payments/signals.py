from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import FeePayment
from notifications.services import send_sms_notification
from django.conf import settings
from payments.utils import generate_receipt_pdf

@receiver(post_save, sender=FeePayment)
def notify_parent_on_payment(sender, instance, created, **kwargs):
    if created:
        pdf_relative_path = generate_receipt_pdf(instance)
        instance.receipt_url = f"{settings.MEDIA_URL}{pdf_relative_path}"
        instance.save()

        full_url = f"{settings.SITE_URL}{instance.receipt_url}"
        message = f"Dear Parent, your payment of KES {instance.amount_paid} for {instance.student.name} has been received. You can download the receipt here: {full_url}"
        send_sms_notification(instance.parent.phone_number, message)
