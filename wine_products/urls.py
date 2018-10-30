from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.home, name='home'),

    url(r'^categorie/list/$', views.categorie_list, name='categorie_list'),
    url(r'^categorie/add/new$', views.categorie_add, name='categorie_add'),
    url(r'^categorie/(?P<id>\d+)/edit$', views.categorie_add, name='categorie_edit'),

    url(r'^quantity/list/$', views.quantity_list, name='quantity_list'),
    url(r'^quantity/add/new$', views.quantity_add, name='quantity_add'),
    url(r'^quantity/(?P<id>\d+)/edit$', views.quantity_add, name='quantity_edit'),


    url(r'^products/list$', views.product_list, name='product_list'),
    url(r'^products/add/new$', views.product_add, name='product_add'),
    url(r'^products/(?P<id>\d+)/edit$', views.product_add, name='product_edit'),

    
   



]