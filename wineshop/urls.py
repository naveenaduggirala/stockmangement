from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf import settings
# from django.conf.urls import (handler400, handler403, handler404, handler500)
# handler400 = custom_400
# handler403 = custom_403
# handler404 = custom_404
# handler500 = custom_500

urlpatterns = patterns('',
	url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('wine_products.urls')),
)
