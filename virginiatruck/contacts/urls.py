from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^contacts/$', 'contacts.views.ShowContacts'),
)