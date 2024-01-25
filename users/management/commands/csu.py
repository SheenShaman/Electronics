import os

from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email=os.getenv('USER_EMAIL'),
            first_name='Admin',
            last_name='Admin',
            is_staff=True,
            is_superuser=True,
            is_active=True
        )
        user.set_password(os.getenv('USER_PASS'))
        user.save()
