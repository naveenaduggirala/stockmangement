from django.db import models
# from products.base import BaseModel
from wine_products.models import Categorie,Qunatite,Product
from wine_products.base import BaseModel


# Create your models here.

class Stock(BaseModel):
	categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
	products = models.ForeignKey(Product, on_delete=models.CASCADE)
	qunatity = models.ForeignKey(Qunatite, on_delete=models.CASCADE)
	stoct_of_products = models.IntegerField()
	def __str__(self):
		return '%s' % self.products


class Report(BaseModel):
	categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
	products = models.ForeignKey(Product, on_delete=models.CASCADE)
	qunatity = models.ForeignKey(Qunatite, on_delete=models.CASCADE)
	total_count_saled_today = models.IntegerField()
	total_price = models.CharField(max_length=100,blank=True,null=True)

	def __str__(self):
		return '%s' % self.products
