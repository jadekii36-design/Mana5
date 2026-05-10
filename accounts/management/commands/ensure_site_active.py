import os
from datetime import date, timedelta
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Ensure SiteControl exists and is not expired"

    def handle(self, *args, **options):
        from accounts.models import SiteControl

        expiry_str = os.environ.get("SITE_EXPIRY_DATE", "").strip()
        if expiry_str:
            try:
                target_date = date.fromisoformat(expiry_str)
            except ValueError:
                target_date = date.today() + timedelta(days=365)
        else:
            target_date = date.today() + timedelta(days=365)

        ctrl = SiteControl.objects.first()
        if not ctrl:
            SiteControl.objects.create(
                panel_title="Panel System",
                expires_at=target_date,
            )
            self.stdout.write(self.style.SUCCESS(f"SiteControl created with expiry: {target_date}"))
        elif ctrl.is_fully_blocked:
            ctrl.expires_at = target_date
            ctrl.save(update_fields=["expires_at"])
            self.stdout.write(self.style.SUCCESS(f"SiteControl expiry updated to: {target_date}"))
        else:
            self.stdout.write(self.style.SUCCESS(f"SiteControl OK, expires: {ctrl.expires_at}"))
