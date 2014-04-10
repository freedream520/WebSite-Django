from django.db import models

# creando modelos de datos para la aplicacion home
# Creating data models for the application home

class Company(models.Model):
	name = models.CharField(max_length=255)
	phone = models.CharField(max_length=255)
	fax = models.CharField(max_length=255)
	email = models.EmailField()
	address = models.CharField(max_length=300)
	msg = models.TextField()

	def __unicode__(self):
		return self.name


class img_slider_index(models.Model):
	name = models.CharField(max_length=255)
	image = models.ImageField(upload_to='static/images/slider')

	def __unicode__(self):
		return self.name


class img_customers(models.Model):
	name = models.CharField(max_length=255)
	image_url = models.ImageField(upload_to='static/images/customers')

	def __unicode__(self):
		return self.name


class slider_footer(models.Model):
	name = models.CharField(max_length=255)
	image_url = models.ImageField(upload_to='static/images/sliderfooter')

	def __unicode__(self):
		return self.name





