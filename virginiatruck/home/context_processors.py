from .models import Company, slider_footer


# funcion para retornar todas las variables que utilizare repetidas veces en todo el sitio web
# Function to return all who uses variables repeatedly throughout the web site

def my_processor(request):
	company = Company.objects.get(id=1)
	slider_foo = slider_footer.objects.all()
	return {'company':company, 'slider_foo': slider_foo }