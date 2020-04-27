from django.core.management.base import BaseCommand
from pages.models import Invite
import csv


class Command(BaseCommand):
    def handle(self, *args, **options):
        print('Loading CSV')
        csv_path = './academy_invites_2014.csv'
        with open(csv_path, 'rt') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                obj = Invite.objects.create(
                    name=row['Name'],
                    branch=row['Branch']
                )
                print(obj)
