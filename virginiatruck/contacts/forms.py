from django.forms import ModelForm
from django import forms


# creo una tupla para generar el select del formulario con esta tupla    
# Create a tuple to generate select form with this tuple

TITLE_SELECT = (
    ('I am a customer', 'I am a customer'),
    ('Recommended by client', 'Recommended by client'),
    ('Facebook, Twitter', 'Facebook, Twitter'),
    ('Google', 'Google'),
    ('Other','Other')
)

''' creando el formulario de contacto donde se le envia como atributos de 
widget el nombre de la clase para darle formato con boostrap '''

''' creating a contact form where you send as attributes 
The widget class name to format with bootstrap '''

class ContactForm(forms.Form):
	name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter name'}))
	email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter email'}))
	phonenumber = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter phone number'}))
	company = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter name company'}), required=False)
	hyn = forms.CharField(widget=forms.Select(choices=TITLE_SELECT, attrs={'class': 'form-control'}))
	comments = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))


