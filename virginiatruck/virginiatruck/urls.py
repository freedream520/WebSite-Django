from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'virginiatruck.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^', include('home.urls')),

    url(r'^', include('about.urls')),

    url(r'^', include('services.urls')),

    url(r'^', include('products.urls')),

    url(r'^', include('jobs.urls')),

    url(r'^', include('contacts.urls')),
)
