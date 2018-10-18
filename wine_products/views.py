from django.shortcuts import render
from .models import Categorie,Qunatite,Product
from .forms import ProductForm
from django.shortcuts import render_to_response
from django.template import Context, Template
from django.shortcuts import get_list_or_404, get_object_or_404
# Create your views here.


def product_add(request,id=None,product_obj=None,template_name="wine_products/product_add.html"):
	if id:
		product_obj = get_object_or_404(Product, pk=id)
		if request.method == 'POST':
			form = ProductForm(request.POST, instance=product_obj)
			if form.is_valid():
				form.save()
				messages.success(request, 'Product details updated.')
			else:
				print form.errors
		else:
			form = ProductForm(instance=product_obj)

	else:
		print "new form"
		if request.method == 'POST':
			form = ProductForm(request.POST, instance=product_obj)
			if form.is_valid():
				form.save()
				messages.success(request, 'New product saved successfully.')
			else:
				print form.errors
		else:
			form = ProductForm(instance=product_obj)

	
	return render_to_response(template_name,
							 Context(request))
	


