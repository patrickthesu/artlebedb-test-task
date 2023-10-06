from django.core.management.base import BaseCommand, CommandError
from libraries.parser import load_json, parse_json
from backend.settings import DATA_PATH


class Command(BaseCommand):
    help = "Automaticaly scrapp and parse values into database libraries"

    def handle(self, *args, **options):
        print("Loading data...")
        data = load_json(DATA_PATH)
        parse_json(data)        
