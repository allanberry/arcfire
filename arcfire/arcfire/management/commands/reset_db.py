from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = 'Destroys and recreates the development database to a pristine state.'

    # def add_arguments(self, parser):
    #     parser.add_argument('poll_id', nargs='+', type=int)

    def handle(self, *args, **options):
        self.stdout.write("Hello World.", ending='\n')