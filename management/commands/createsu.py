from django.core.management.base import BaseCommand
from authentication.models import CustomUser
from django.conf import settings

class Command(BaseCommand):

    def handle(self, *args, **options):
        if not CustomUser.objects.filter(email=settings.SUPER_USER['email']).exists():
            CustomUser.objects.create_superuser(email=settings.SUPER_USER['email'], password=settings.SUPER_USER['password'])
