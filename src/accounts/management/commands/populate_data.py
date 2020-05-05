from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        print("Populating data")
        from django.core.management import call_command
        call_command('loaddata', 'db.json', app_label='myapp')
