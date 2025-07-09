from django.http import JsonResponse
from payments.models import FeeBalance
from .services import send_sms_notification

def send_debt_reminders(request):
    count = 0
    for balance in FeeBalance.objects.all():
        if balance.balance > 0:
            message = f"Dear Parent, your fee balance is KES {balance.balance}. Please clear it soon."
            send_sms_notification(balance.parent.phone_number, message)
            count += 1
    return JsonResponse({'status': 'reminders sent', 'total': count})

# Git commit message:
# "Add view to send SMS reminders for fee balances"