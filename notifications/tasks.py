from .services import send_sms_notification
from payments.models import FeeBalance

def remind_parents_with_debt():
    for balance in FeeBalance.objects.all():
        if balance.balance > 0:            
            message = f"Dear Parent, your school fee balance is KES {balance.balance}. Kindly ensure that it is cleared before the end of the term. Thank you."
            send_sms_notification(balance.parent.phone_number, message)
