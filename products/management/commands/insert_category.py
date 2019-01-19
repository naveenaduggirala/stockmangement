from django.core.management.base import BaseCommand, CommandError
from products.models import Categorie,Qunatite

class Command(BaseCommand):
    help = 'Inser Categories'

    def handle(self, *args, **options):
        categories_list = ['Beer','wisky','vadka','rum']
        for each_obj in categories_list:
        	kwargs = {
        	"name":each_obj.lower(),
        	"label_name":each_obj.capitalize() 
        	}
        	cat_obj = Categorie.objects.create(**kwargs)