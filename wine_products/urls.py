from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^products/new/add$', views.product_add, name='product_add'),
    url(r'^products/(?P<id>\d+)/edit$', views.product_add, name='product_edit'),
]