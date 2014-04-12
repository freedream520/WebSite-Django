from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^products/$', 'products.views.ShowProducts'),
    url(r'^products/ajax_products/$','products.views.ajaxProducts'),
)
