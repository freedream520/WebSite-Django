from django.shortcuts import render
from .models import about

def ShowAbout(request):
	abt = about.objects.get(id=1)
	return render(request, 'about/about.html', {'abt':abt})
