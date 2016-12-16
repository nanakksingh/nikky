from django.core.management.base import BaseCommand, CommandError
from shortner.models import DockURL
class Command(BaseCommand):
    help = 'Refreshes all DockURL shortcodes'

    def add_arguments(self, parser):
        parser.add_argument('items',type=int)

    def handle(self, *args, **options):
        return DockURL.objects.refresh_shortcodes(items=options['items'])

        