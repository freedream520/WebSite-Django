from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from .models import categoryProd, products

def ShowProducts(request):
	catProd = categoryProd.objects.all()
	return render(request,'products/products.html',{ 'catProd' : catProd })

# esta funcion recibe la peticion ajax y devuelve los productos que pertenecen a esa categoria
# This function receives the ajax request and returns the products that belong to the category

def ajaxProducts(request):
	id_categoryprod = request.GET['id']
	products_list = products.objects.filter(id_categoryprod = id_categoryprod)
	data = serializers.serialize('json', products_list, fields=('name'))
	return HttpResponse(data, mimetype='application/json')
