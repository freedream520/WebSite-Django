from django.shortcuts import render_to_response
#from .models import about

def ShowProducts(request):
	return render_to_response('jobs/jobs.html')

