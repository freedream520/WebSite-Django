from django.db import models

# creando modelos de datos para la aplicacion products
# Creating data models for the application products

class categoryProd(models.Model):
	name = models.CharField(max_length=255)

	def __unicode__(self):
		return self.name

class products(models.Model):
	name = models.CharField(max_length=255)
	id_categoryprod = models.ForeignKey('categoryProd')

	def __unicode__(self):
		return self.name
