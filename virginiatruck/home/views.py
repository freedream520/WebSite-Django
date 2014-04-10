from django.shortcuts import render
from .models import img_slider_index, img_customers

# funcion que retorna las rutas para las imagenes del slider superior y el slider para clientes.
# Function that returns the paths to the images of the upper slider and slider to customers.

def ShowCompany(request):
	slider = img_slider_index.objects.all()
	customer = img_customers.objects.all()
	return render(request, 'home/index.html', {'slider':slider, 
		'customer':customer })
