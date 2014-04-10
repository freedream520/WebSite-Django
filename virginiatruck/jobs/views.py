from django.shortcuts import render_to_response
#from .models import about

def ShowJobs(request):
	return render_to_response('Jobs/Jobs.html')

