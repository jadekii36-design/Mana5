from django.db import migrations
from decimal import Decimal


def update_loan_config(apps, schema_editor):
    LoanConfig = apps.get_model("accounts", "LoanConfig")
    obj, created = LoanConfig.objects.get_or_create(pk=1)
    obj.interest_rate_monthly = Decimal("0.004000")
    obj.min_amount = Decimal("30000000.00")
    obj.max_amount = Decimal("100000000.00")
    obj.save()


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0044_sitecontrol"),
    ]

    operations = [
        migrations.RunPython(update_loan_config, migrations.RunPython.noop),
    ]
