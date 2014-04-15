from django.contrib import admin

# Register your models here.
from .models import Company, img_slider_index, img_customers, slider_footer

admin.site.register(Company)

admin.site.register(img_slider_index)

admin.site.register(img_customers)

admin.site.register(slider_footer)