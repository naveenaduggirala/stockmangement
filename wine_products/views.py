from django.shortcuts import render
from .models import Categorie,Qunatite,Product
from .forms import ProductForm,UserLoginForm
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

	
	return render_to_response(template_name,
							 Context(request))

def user_login(request, template_name="wine_products/login.html"):
	if request.method == "POST":
		print "logins"
		form = UserLoginForm(request.POST)
		if form.is_valid():
			try:
				user_profile = User.objects.get(username=form.cleaned_data['username'], is_active=True)
				if not user_profile.check_password(form.cleaned_data['password']):
					messages.warning(request, 'Invalid Login Details')
					return HttpResponseRedirect(reverse('login_page'))
			except User.DoesNotExist as e:
				messages.warning(request, 'Invalid Login Details')
				return HttpResponseRedirect(reverse('login_page'))
			backend = get_backends()[0]
			user_profile.backend = "%s.%s" % (backend.__module__, backend.__class__.__name__)
			login(request, user_profile)
			try:
				request.session.pop("prev_logged_in_user")
			except KeyError as e:
				pass
			if request.user.is_superuser:
				return HttpResponseRedirect(reverse('product_add'))
			else:
				pass
		else:
			print form.errors
	else:
		form = UserLoginForm()
		logout(request)

	variables = {
		"page_title": "Login",
		"form" : form
	}
	return render_to_response(template_name,
							  RequestContext(request, variables))


	


