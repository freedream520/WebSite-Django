from django.core.mail import send_mail
from django.shortcuts import render
from django.http import  HttpResponseRedirect
from django.template import RequestContext
from .forms import ContactForm
from django.core.mail import EmailMessage


''' creando la funcion que recibe los valores de los campos para procesarlos y luego enviarlos en un email '''

def contacts(request):
	if request.method == 'POST':
		formc = ContactForm(request.POST)
		if formc.is_valid():
			title = "Email from WebSite"
			content = "Name: " + formc.cleaned_data['name'] + "\n"
			content += "Email: " + formc.cleaned_data['email'] + "\n"
			content += "Phone Number: " + formc.cleaned_data['phonenumber'] + "\n"
			content += "Company Name: " + formc.cleaned_data['company'] + "\n"
			content += "As we know: " + formc.cleaned_data['hyn'] + "\n"
			content += "Comments: " + formc.cleaned_data['comments']

			to_mail = EmailMessage( title, content, to=['dennyssolis@gmail.com']) # direccion donde se enviara el correo.
			to_mail.send()
			return HttpResponseRedirect('/')
	else:
		formc = ContactForm()
	return render(request, 'contacts/contacts.html',{'formc' : formc},context_instance=RequestContext(request))


