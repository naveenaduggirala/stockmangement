from django.db import models
from products.models import Categorie,Qunatite,Product
from products.base import BaseModel


# Create your models here.

class Stock(BaseModel):
	categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
	products = models.ForeignKey(Product, on_delete=models.CASCADE)
	qunatity = models.ForeignKey(Qunatite, on_delete=models.CASCADE)
	stock = models.PositiveIntegerField(blank=True,null=True)
	stock_receive_date = models.DateTimeField(blank=True,null=True)
	def __str__(self):
		return '%s' % self.products


class DailyMasters(BaseModel):
	categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
	products = models.ForeignKey(Product, on_delete=models.CASCADE)
	qunatity = models.ForeignKey(Qunatite, on_delete=models.CASCADE)
	opening_balance = models.PositiveIntegerField(blank=True,null=True)
	closing_balance = models.PositiveIntegerField(blank=True,null=True)

	def __str__(self):
		return '%s' % self.products

class DailySales(BaseModel):
	categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
	products = models.ForeignKey(Product, on_delete=models.CASCADE)
	qunatity = models.ForeignKey(Qunatite, on_delete=models.CASCADE)
	count = models.CharField(max_length=100,blank=True,null=True)
	soled_on = models.DateField(blank=True,null=True)

	def __str__(self):
		return '%s' % self.products
