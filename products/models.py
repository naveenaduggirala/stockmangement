from django.db import models
from django.utils import timezone
from products.base import BaseModel
# Create your models here.


class Categorie(BaseModel):
	name = models.CharField(max_length=50,unique=True)
	label_name = models.CharField(blank=True,null=True,max_length=50)

	def __str__(self):
		return '%s' % self.name

class Qunatite(BaseModel):
	name = models.CharField(max_length=50,unique=True)
	label_name = models.CharField(blank=True,null=True,max_length=50)
	code = models.CharField(max_length=50)

	def __str__(self):
		return '%s' % self.name

class Product(BaseModel):
	name = models.CharField(max_length=50,unique=True)
	code = models.CharField(max_length=50)
	label_name = models.CharField(blank=True,null=True,max_length=50)
	products_categorie = models.ForeignKey(Categorie,blank=True,null=True)
	quantity = models.ForeignKey(Qunatite,blank=True,null=True)
	price = models.CharField(blank=True,null=True,max_length=50)

	def __str__(self):
		return '%s' % self.name


