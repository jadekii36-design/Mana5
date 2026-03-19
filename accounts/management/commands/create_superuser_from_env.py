import os
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = "Create superuser from environment variables if not exists"

    def handle(self, *args, **options):
        User = get_user_model()
        phone = os.environ.get("DJANGO_SUPERUSER_PHONE")
        password = os.environ.get("DJANGO_SUPERUSER_PASSWORD")

        if not phone or not password:
            self.stdout.write(self.style.WARNING(
                "DJANGO_SUPERUSER_PHONE or DJANGO_SUPERUSER_PASSWORD not set. Skipping."
            ))
            return

        if User.objects.filter(phone=phone).exists():
            self.stdout.write(self.style.SUCCESS(
                f"Superuser with phone {phone} already exists."
            ))
            return

        User.objects.create_superuser(phone=phone, password=password)
        self.stdout.write(self.style.SUCCESS(
            f"Superuser created with phone: {phone}"
        ))
