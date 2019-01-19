from django.core.management.base import BaseCommand, CommandError
from products.models import Categorie,Qunatite,Product
from django.conf import settings
import csv 

class Command(BaseCommand):
    help = 'read the data from csv and insert into database table'

    def handle(self, *args, **options):
        file_name = settings.MEDIA_ROOT+"/"+'products'+"/"+'products.csv'
        headers = [] 
        row_data = [] 
        with open(file_name, 'r') as csvfile: 
            csvreader = csv.reader(csvfile) 
            headers = csvreader.next() 
            for row in csvreader: 
                row_data.append(row) 
            for each_row in row_data:
                prod_cat = Categorie.objects.get(name=each_row[2])
                quantity = Qunatite.objects.get(name=each_row[3])
                kwargs={
                "name":each_row[0],
                "code":each_row[1],
                "label_name":each_row[0].capitalize(),
                "products_categorie":prod_cat,
                "quantity":quantity,
                "price":each_row[4]
                }
                print kwargs
                Product.objects.create(**kwargs)



