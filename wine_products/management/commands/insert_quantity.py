from django.core.management.base import BaseCommand, CommandError
from wine_products.models import Categorie
import random
import enum 

class Command(BaseCommand):
    help = 'Inser Categories'

    def handle(self, *args, **options):
        quantity_list = ['750','375','180','60','90']
        quantity_codes = ['01','02','03','04','05']
        for qu_in,qu_val in enumerate(quantity_list):
            print qu_in,qu_val
            print qu_in[quantity_codes]
            kwargs={
            "name":qu_val,
            "label_name":qu_val,
            "code":qu_in[quantity_codes]
            }
        print kwargs
