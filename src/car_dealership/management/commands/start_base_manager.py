from django.core.management.base import BaseCommand

from src.car_dealership.managers.base_manager import start


class Command(BaseCommand):
    """Start base_manager script"""
    def handle(self, *args, **options):
        start.handle()
        return "Script successfully complete"
