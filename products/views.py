from django.shortcuts import render,HttpResponseRedirect
from django.core.urlresolvers import resolve,reverse
from .models import Categorie,Qunatite,Product
from reports.models import *
from .forms import ProductForm,UserLoginForm,CategorieForm,QuantityForm,StockForm,SalesForm
from django.shortcuts import render_to_response
from django.template import Context, Template
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, get_backends, authenticate
from django.template import RequestContext
from django.contrib import messages


# Create your views here.

@login_required
def home(request,template_name="home.html"):
	return render_to_response(template_name,
							 RequestContext(request))

@login_required
def logout(request):
	logout(request)



@login_required
def categorie_list(request,template_name="products/categorie_list.html"):
	categorie_list = Categorie.objects.all()
	categorie_obj_dict={
	"categorie_list":categorie_list,
	"page_title":"categories"
	}
	return render_to_response(template_name,
							 RequestContext(request,categorie_obj_dict))

@login_required
def categorie_add(request,id=None,categorie_obj=None,template_name="products/categorie_add.html"):
	if id:
		categorie_obj = Categorie.objects.get(pk=id)
		if request.method == 'POST':
			form = CategorieForm(request.POST, instance=categorie_obj)
			if form.is_valid():
				form.save()
				messages.success(request, 'Categorie edited successfully')
				return HttpResponseRedirect(reverse('categorie_list'))
			else:
				print form.errors
		else:
			form = CategorieForm(instance=categorie_obj)

	else:
		if request.method == 'POST':
			form = CategorieForm(request.POST, instance=categorie_obj)
			if form.is_valid():
				form.save()
				messages.success(request, 'Categorie added successfully')
				return HttpResponseRedirect(reverse('categorie_list'))

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
def product_list(request,template_name="products/products_list.html"):
	product_list = Product.objects.all()
	product_obj_dict={
	"product_list":product_list,
	
	}
	return render_to_response(template_name,
							 RequestContext(request,product_obj_dict))

@login_required
def product_add(request,id=None,product_obj=None,template_name="products/product_add.html"):
	if id:
		product_obj = Product.objects.get(pk=id)
		if request.method == 'POST':
			form = ProductForm(request.POST, instance=product_obj)
			if form.is_valid():
				form.save()
			else:
				print form.errors
			
			if not id:
				messages.success(request, 'Product details edited successfully.')
			else:
				messages.success(request, 'Product details saved successfully.')

			return HttpResponseRedirect(reverse('product_list'))


		else:
			form = ProductForm(instance=product_obj)

	else:
		if request.method == 'POST':
			form = ProductForm(request.POST, instance=product_obj)
			if form.is_valid():
				form.save()
				messages.success(request, 'New product saved successfully.')
				return HttpResponseRedirect(reverse('categorie_list'))
			else:
				print form.errors
		else:
			form = ProductForm(instance=product_obj)

	product_form_dict ={
	"form":form,
	"product_obj":product_obj
	}

	
	return render_to_response(template_name,product_form_dict,
							 RequestContext(request))

@login_required
def quantity_list(request,template_name="products/quantity_list.html"):
	quantity_obj_list = Qunatite.objects.all()
	quantity_list_dict ={
	"quantity_list":quantity_obj_list
	}
	return render_to_response(template_name,quantity_list_dict,RequestContext(request))

@login_required
def quantity_add(request,id=None,qunatite_obj=None,template_name="products/quantity_add.html"):
	if id:
		qunatite_obj = Qunatite.objects.get(pk=id)
	if request.method == 'POST':
		form = QuantityForm(request.POST,instance=qunatite_obj)
		if form.is_valid():
			form.save()
		else:
			print form.errors

		if not id:
			messages.success(request, 'Qunatite created successfully')
		else:
			messages.success(request, 'Qunatite edited successfully')
		return HttpResponseRedirect(reverse('quantity_list'))


	else:
		form = QuantityForm(instance=qunatite_obj)

	qunatity_form_dict ={
	"form":form,
	"qunatite_obj":qunatite_obj
	}

	return render_to_response(template_name,qunatity_form_dict,RequestContext(request))

@login_required
def stock_add(request,id=None,stock_obj=None,template_name="products/stock_add.html"):
	if id:
		stock_obj = Stock.objects.get(pk=id)
	if request.method == 'POST':
		form = StockForm(request.POST,instance=stock_obj)
		if form.is_valid():
			stock_obj = form.save()
			kwargs = {
					  "categorie":stock_obj.categorie,
					  "products":stock_obj.products,
					  "qunatity":stock_obj.qunatity
					  }
			try:
				da_ma_obj = DailyMasters.objects.get(**kwargs)
				da_ma_obj.opening_balance = da_ma_obj.opening_balance+stock_obj.stock
				da_ma_obj.closing_balance = da_ma_obj.closing_balance+stock_obj.stock
				da_ma_obj.save()
			except DailyMasters.DoesNotExist as e:
				da_ma_obj = DailyMasters.objects.create(categorie=stock_obj.categorie,products=stock_obj.products,qunatity=stock_obj.qunatity,opening_balance=stock_obj.stock,closing_balance=stock_obj.stock)
		else:
			print form.errors

		if not id:
			messages.success(request,"Stock added successfully")
		else:
			messages.success(request,"Stock edited successfully")
		return HttpResponseRedirect(reverse('stock_list'))
	else:
		form = StockForm(instance=stock_obj)

	stock_form_dict = {
	"form":form,
	"stock_obj":stock_obj
	}
	return render_to_response(template_name,stock_form_dict,RequestContext(request))


@login_required
def stock_list(request,template_name="products/stock_list.html"):
	stock_obj_list = Stock.objects.all()
	stock_obj_dict={
	"stock_obj":stock_obj_list
	}
	return render_to_response(template_name,stock_obj_dict,RequestContext(request))

@login_required
def sales_list(request,template_name="products/sales_list.html"):
	daily_sales_obj_list = DailySales.objects.all()
	daily_sales_obj_dict={
	"daily_sales_obj":daily_sales_obj_list
	}
	return render_to_response(template_name,daily_sales_obj_dict,RequestContext(request))

@login_required
def sales_add(request,id=None,sales_obj=None,template_name="products/sales_add.html"):
	if id:
		sales_obj = DailySales.objects.get(pk=id)
	if request.method == 'POST':
		form = SalesForm(request.POST,instance=sales_obj)
		if form.is_valid():
			#validation for selling products based on stock
			categorie = form.cleaned_data['categorie']
			products = form.cleaned_data['products']
			qunatity = form.cleaned_data['qunatity']

			kwargs = {
					"categorie":categorie,
					"products":products,
					"qunatity":qunatity
					}
			try:
				da_ma_obj = DailyMasters.objects.get(**kwargs)
			except DailyMasters.DoesNotExist as e:
				print (e)

			to_sell_count = form.cleaned_data['count']

			if to_sell_count > da_ma_obj.opening_balance:
				messages.warning(request,"Unable to sell the product.Your stock is insufficent")
				return HttpResponseRedirect(reverse('sales_add'))
			else:
				sales_obj = form.save()

				# kwargs = {
				# 		  "categorie":sales_obj.categorie,
				# 		  "products":sales_obj.products,
				# 		  "qunatity":sales_obj.qunatity
				# 		  }
				# try:
				# 	da_ma_obj = DailyMasters.objects.get(**kwargs)
				# 	da_ma_obj.opening_balance = da_ma_obj.opening_balance-int(sales_obj.count)
				# 	da_ma_obj.closing_balance = da_ma_obj.closing_balance-int(sales_obj.count)	
				# 	da_ma_obj.save()
				# except DailyMasters.DoesNotExist as e:
				# 	print (e)

				da_ma_obj.opening_balance = da_ma_obj.opening_balance-int(sales_obj.count)
				da_ma_obj.closing_balance = da_ma_obj.closing_balance-int(sales_obj.count)	
				da_ma_obj.save()

			if not id:
				messages.success(request,"Product saled successfully")
			else:
				messages.success(request,"Product saled edited successfully")
				return HttpResponseRedirect(reverse('sales_list'))
		else:
			print form.errors

		
	else:
		form = SalesForm(instance=sales_obj)

	sales_form_dict = {
	"form":form,
	"sales_obj":sales_obj
	}
	return render_to_response(template_name,sales_form_dict,RequestContext(request))



@login_required
def masters_list(request,template_name="products/stock_details.html"):
	stock_deatils_list = DailyMasters.objects.all()
	stock_deatils_dict={
	"stock_deatils_list":stock_deatils_list
	}
	return render_to_response(template_name,stock_deatils_dict,RequestContext(request))

