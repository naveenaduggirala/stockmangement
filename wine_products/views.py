from django.shortcuts import render
from .models import Categorie,Qunatite,Product
from .forms import ProductForm,UserLoginForm,CategorieForm,QuantityForm
from django.shortcuts import render_to_response
from django.template import Context, Template
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, get_backends, authenticate
from django.template import RequestContext

# Create your views here.

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
		categorie_obj = Categorie.objects.get(pk=id)
		if request.method == 'POST':
			form = CategorieForm(request.POST, instance=categorie_obj)
			if form.is_valid():
				form.save()
			else:
				print form.errors
		else:
			form = CategorieForm(instance=categorie_obj)

	else:
		if request.method == 'POST':
			form = CategorieForm(request.POST, instance=categorie_obj)
			if form.is_valid():
				form.save()
			else:
				print form.errors
		else:
			form = CategorieForm(instance=categorie_obj)

	categorie_form_dict={
	"form":form,
	"page_title":"Add Categorie",
	"categorie_obj":categorie_obj
	}

	return render_to_response(template_name,categorie_form_dict,
							 RequestContext(request))

@login_required
def product_list(request,template_name="wine_products/products_list.html"):
	product_list = Product.objects.all()
	product_obj_dict={
	"product_list":product_list,
	
	}
	return render_to_response(template_name,
							 RequestContext(request,product_obj_dict))

@login_required
def product_add(request,id=None,product_obj=None,template_name="wine_products/product_add.html"):
	if id:
		product_obj = Product.objects.get(pk=id)
		if request.method == 'POST':
			form = ProductForm(request.POST, instance=product_obj)
			if form.is_valid():
				form.save()
				# messages.success(request, 'Product details updated.')
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
				# messages.success(request, 'New product saved successfully.')
			else:
				print form.errors
		else:
			form = ProductForm(instance=product_obj)
			print form,"form"

	product_form_dict ={
	"form":form,
	"product_obj":product_obj
	}

	
	return render_to_response(template_name,product_form_dict,
							 RequestContext(request))

@login_required
def quantity_list(request,template_name="wine_products/quantity_list.html"):
	quantity_obj_list = Qunatite.objects.all()
	quantity_list_dict ={
	"quantity_list":quantity_obj_list
	}
	return render_to_response(template_name,quantity_list_dict,RequestContext(request))


def quantity_add(request,id=None,qunatite_obj=None,template_name="wine_products/quantity_add.html"):
	if id:
		qunatite_obj = Qunatite.objects.get(pk=id)
		print "id"
		print qunatite_obj,"qunatite_obj"
	if request.method == 'POST':
		form = QuantityForm(request.POST,instance=qunatite_obj)
		print form,"form"
		if form.is_valid():
			form.save()
		else:
			print form.errors
	else:
		form = QuantityForm(instance=qunatite_obj)
		print form,"form"

	qunatity_form_dict ={
	"form":form,
	"qunatite_obj":qunatite_obj
	}

	return render_to_response(template_name,qunatity_form_dict,RequestContext(request))







