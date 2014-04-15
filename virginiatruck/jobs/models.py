from django.db import models

# creando modelos de datos para la aplicacion jobs
# Creating data models for the application jobs

class jobs(models.Model):
	title = models.CharField(max_length=255)
	content = models.TextField()
	compensation= models.CharField(max_length=255)

	def __unicode__(self):
		return self.title