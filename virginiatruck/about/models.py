from django.db import models

# creando modelos de datos para la aplicacion home
# Creating data models for the application home

class about(models.Model):
	title = models.CharField(max_length=255)
	content = models.TextField()
	url_image = models.ImageField(upload_to='static/images/about')

	def __unicode__(self):
		return self.title