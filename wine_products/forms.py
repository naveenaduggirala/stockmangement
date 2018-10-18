from django import forms
from .models import Categorie,Qunatite,Product

class ProductForm(forms.ModelForm):
	def __init__(self,*args,**kwargs):
		super(ProductForm, self).__init__(*args, **kwargs)
	class Meta:
		model = Product
		exclude = ()