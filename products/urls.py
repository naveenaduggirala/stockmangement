from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.home, name='home'),
    url(r'^logout$', views.logout, name='logout_user'),


    url(r'^categorie/list/$', views.categorie_list, name='categorie_list'),
    url(r'^categorie/add/new$', views.categorie_add, name='categorie_add'),
    url(r'^categorie/(?P<id>\d+)/edit$', views.categorie_add, name='categorie_edit'),

    url(r'^quantity/list/$', views.quantity_list, name='quantity_list'),
    url(r'^quantity/add/new$', views.quantity_add, name='quantity_add'),
    url(r'^quantity/(?P<id>\d+)/edit$', views.quantity_add, name='quantity_edit'),


    url(r'^products/list$', views.product_list, name='product_list'),
    url(r'^products/add/new$', views.product_add, name='product_add'),
    url(r'^products/(?P<id>\d+)/edit$', views.product_add, name='product_edit'),

    
    url(r'^stock/list$', views.stock_list, name='stock_list'),
    url(r'^stock/add/new$', views.stock_add, name='stock_add'),
    url(r'^stock/(?P<id>\d+)/edit$', views.stock_add, name='stock_edit'),

    url(r'^sales/list$', views.sales_list, name='sales_list'),
    url(r'^sales/add/new$', views.sales_add, name='sales_add'),
    url(r'^sales/(?P<id>\d+)/edit$', views.stock_add, name='sales_edit'),

    url(r'^masters/list$', views.masters_list, name='masters_list'),

    
   



]