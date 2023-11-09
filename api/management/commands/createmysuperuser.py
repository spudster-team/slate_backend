from django.core.management.base import BaseCommand

from api.models import User


# create superuser
class Command(BaseCommand):
    def handle(self, *args, **options):
        User.objects.create_superuser(
            email="admin@gmail.com", password="@bcd1234", first_name="admin", last_name="admin"
        )
