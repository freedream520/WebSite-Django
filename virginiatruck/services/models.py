from django.db import models

# creando modelos de datos para la aplicacion services
# Creating data models for the application services

class services(models.Model):
	description = models.TextField()

	def __unicode__(self):
		return self.description