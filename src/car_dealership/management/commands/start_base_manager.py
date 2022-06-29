from django.core.management.base import BaseCommand

from car_dealership.managers import base_manager


class Command(BaseCommand):
    """Start base_manager script"""
    def handle(self, *args, **options):
        create_info = base_manager.start()
        return "Script successfully complete"
