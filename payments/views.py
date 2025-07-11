from django.http import HttpResponse
from django.template.loader import render_to_string
import weasyprint
from users.models import Student

def student_balance_pdf(request, student_id):
    student = Student.objects.get(id=student_id)
    total_paid = sum(payment.amount_paid for payment in student.feepayment_set.all())
    total_fee = student.total_fee 
    balance = total_fee - total_paid

    html = render_to_string("", {
        "student": student,
        "total_paid": total_paid,
        "total_fee": total_fee,
        "balance": balance,
    })

    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = f"inline; filename=balance_{student.id}.pdf"
    weasyprint.HTML(string=html).write_pdf(response)
    return response
