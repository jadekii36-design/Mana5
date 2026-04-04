from django.db import migrations
from decimal import Decimal, InvalidOperation


def recalculate_repayments(apps, schema_editor):
    LoanApplication = apps.get_model("accounts", "LoanApplication")
    for loan in LoanApplication.objects.exclude(
        amount=None
    ).exclude(term_months=None).exclude(interest_rate_monthly=None):
        try:
            amount = Decimal(str(loan.amount))
            n = Decimal(str(loan.term_months))
            r = Decimal(str(loan.interest_rate_monthly))
            if n > 0:
                loan.monthly_repayment = (amount / n) + (amount * r)
                loan.save(update_fields=["monthly_repayment"])
        except (InvalidOperation, Exception):
            continue


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0045_update_loanconfig_values"),
    ]

    operations = [
        migrations.RunPython(recalculate_repayments, migrations.RunPython.noop),
    ]
