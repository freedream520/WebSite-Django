from django.shortcuts import render
from .models import jobs

# funcion que retorna la lista de los empleos
# Function that returns the list of jobs
def ShowJobs(request):
	list_jobs = jobs.objects.all()
	return render(request,'Jobs/Jobs.html',{'list_jobs' : list_jobs})

