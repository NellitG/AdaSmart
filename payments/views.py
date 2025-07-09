from django.shortcuts import render
from django.http import JsonResponse
from users.models import User
from .models import FeePayment
from notifications.services import send_sms_notification
from .utils import generate_receipt_pdf


def test_payment_entry(request):
    try:
        parent = User.objects.filter(role='parent').first()
        if not parent:
            return JsonResponse({'error': 'No parent user found'}, status=404)
        
        payment = FeePayment.objects.create(
            parent=parent,
            student_name = "Test Student",
            amount_paid = 1000,
            payment_method = 'MPesa',
        )

        # Generate PDF and store the receipt URL
        pdf_relative_path = generate_receipt_pdf(payment)
        payment.receipt_url = f"media/{pdf_relative_path}"
        payment.save()

        # Send SMS with receipt link
        full_url = f"http://127.0.0.1:8000/{payment.receipt_url}"
        msg = f"Dear Parent, we have received your payment of Ksh {payment.amount_paid} for {payment.student_name}. You can download the receipt here: {full_url}"
        send_sms_notification(parent.phone_number, msg)

        return JsonResponse({
            'status': 'success',
            'receipt': full_url})
    
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)