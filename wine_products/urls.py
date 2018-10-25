from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.home, name='home'),

    url(r'^categorie/list/$', views.categorie_list, name='categorie_list'),
    url(r'^categorie/add/new$', views.categorie_add, name='categorie_add'),
    url(r'^categorie/(?P<id>\d+)/edit$', views.categorie_add, name='categorie_edit'),

    url(r'^products/list$', views.product_list, name='product_list'),
    url(r'^products/add/new$', views.product_add, name='product_add'),
    url(r'^products/(?P<id>\d+)/edit$', views.product_add, name='product_edit'),

]