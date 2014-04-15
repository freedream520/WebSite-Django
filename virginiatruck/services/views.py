from django.shortcuts import render
from .models import services

def ShowServices(request):
	servi = services.objects.all() 
	return render(request,'services/services.html',{ 'servi':servi })

