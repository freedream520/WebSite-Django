from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^services/$', 'services.views.ShowServices'),
)
