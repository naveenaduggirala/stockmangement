from django.shortcuts import render
from .models import Categorie,Qunatite,Product
from .forms import ProductForm,UserLoginForm,CategorieForm
from django.shortcuts import render_to_response
from django.template import Context, Template
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, get_backends, authenticate
from django.template import RequestContext

# Create your views here.

@login_required
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
			print form,"form"

	
	return render_to_response(template_name,
							 Context(request))

@login_required
def home(request,template_name="home.html"):
	return render_to_response(template_name,
							 RequestContext(request))


@login_required
def categorie_list(request,template_name="wine_products/categorie_list.html"):
	categorie_list = Categorie.objects.all()
	categorie_obj_dict={
	"categorie_list":categorie_list,
	"page_title":"categories"
	}
	return render_to_response(template_name,
							 RequestContext(request,categorie_obj_dict))

@login_required
def categorie_add(request,id=None,categorie_obj=None,template_name="wine_products/categorie_add.html"):
	if id:
		categorie_obj = get_object_or_404(Product, pk=id)
		if request.method == 'POST':
			form = CategorieForm(request.POST, instance=categorie_obj)
			if form.is_valid():
				form.save()
				messages.success(request, 'Categorie details updated.')
			else:
				print form.errors
		else:
			form = CategorieForm(instance=categorie_obj)

	else:
		print "new form"
		if request.method == 'POST':
			form = CategorieForm(request.POST, instance=categorie_obj)
			if form.is_valid():
				print "form vallid"
				form.save()
				print "form save"
				messages.success(request, 'New Categorie saved successfully.')
			else:
				print form.errors
		else:
			form = CategorieForm(instance=categorie_obj)
			print form,"form"

	categorie_form_dict={
	"form":form,
	"page_title":"Add Categorie",
	"categorie_obj":categorie_obj
	}

	return render_to_response(template_name,
							 RequestContext(request))






	


