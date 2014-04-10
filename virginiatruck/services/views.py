from django.shortcuts import render_to_response
#from .models import about

def ShowServices(request):
	return render_to_response('services/services.html')

