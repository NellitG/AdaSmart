from django.apps import AppConfig


def ready(self):
    import payments.signals
   
class PaymentsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'payments'
