from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'home.views.ShowCompany'),
    url(r'^home/$', 'home.views.ShowCompany'),
)
