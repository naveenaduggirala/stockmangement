from django.core.management.base import BaseCommand, CommandError
from wine_products.models import Categorie,Qunatite
import csv 

class Command(BaseCommand):
    help = 'read the data from csv and insert into database table'

    def handle(self, *args, **options):
        file_name = "/home/user/projects/stockmangement/media/quantites/quantities.csv"
        headers = [] 
        row_data = [] 
        with open(file_name, 'r') as csvfile: 
            csvreader = csv.reader(csvfile) 
            headers = csvreader.next() 
            print headers
            for row in csvreader: 
                row_data.append(row) 
            for each_row in row_data:
                kwargs={
                "name":each_row[0],
                "label_name":each_row[1],
                "code":each_row[2]

                }
                Qunatite.objects.create(**kwargs)



