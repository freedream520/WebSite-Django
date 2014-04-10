from django.shortcuts import render_to_response
#from .models import about

def ShowContacts(request):
	return render_to_response('contacts/contacts.html')

