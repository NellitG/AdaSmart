import os
from django.conf import settings
from django.template.loader import render_to_string
from weasyprint import HTML

def generate_receipt_pdf(payment):
    html_string = render_to_string('receipts/receipt.html', {'payment': payment})
    receipt_dir = os.path.join(settings.MEDIA_ROOT, 'receipts')
    os.makedirs(receipt_dir, exist_ok=True)

    filename = f'receipt_{payment.id}.pdf'
    file_path = os.path.join(receipt_dir, filename)
    HTML(string=html_string).write_pdf(file_path)

    return f"receipts/{filename}"
