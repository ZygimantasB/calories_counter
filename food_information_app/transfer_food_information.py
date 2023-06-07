import pandas as pd
from django.core.management.base import BaseCommand
from food_information_app.models import ProductInformation


class Command(BaseCommand):
    help = "Transfer data from csv file to database"

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str)

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']
        data = pd.read_csv(csv_file)

        for _, row in data.itertuples():
            ProductInformation.objects.create(name=row['name'],
                                              serving_size=row['serving_size'],
                                              calories=row['calories'],
                                              total_protein=row['total_protein'],
                                              total_fat=row['total_fat'],
                                              total_carbohydrate=row['total_carbohydrate'])
