from django.core.management.base import BaseCommand, CommandError
from libraries.parser import get_data
from backend.settings import DATA_PATH, SCRAPPING_PAGE_URL


class Command(BaseCommand):
    help = "Automaticaly scrapp and parse values into database libraries"

    def handle(self, *args, **options):
        print("Scrapping data...")
        get_data (SCRAPPING_PAGE_URL, DATA_PATH)
