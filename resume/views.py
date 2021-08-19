from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from .forms import ContactForm
from django.shortcuts import render, redirect

# Create your views here.
def home(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			form.save()
			subject = "Website Inquiry"
			body = {
				'name':"Name: " + form.cleaned_data['Name'],
				'job_description': "job description: " +form.cleaned_data['job_description'],
				'email': "email address: " + form.cleaned_data['email'],

			}
			message = "\n".join(body.values())
			messages.success(request, 'form submitted successfully')
			try:
				send_mail(subject, message, 'adebaicy@gmail.com', ['adebaicy@gmail.com'])
			except BadHeaderError:
				return HttpResponse('Invalid header found.')
			return redirect("home")

	form = ContactForm()
	return render(request, 'resume/hw.html', {'form': form})


def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			form.save()
			subject = "Website Inquiry"
			body = {
				'name':"Name: " + form.cleaned_data['Name'],
				'job_description': "job description: " +form.cleaned_data['job_description'],
				'email': "email address: " + form.cleaned_data['email'],

			}
			message = "\n".join(body.values())

			try:
				send_mail(subject, message, 'adebaicy@gmail.com', ['adebaicy@gmail.com'])
			except BadHeaderError:
				return HttpResponse('Invalid header found.')
			return redirect("home")

	form = ContactForm()
	return render(request, "resume/contact.html", {'form': form})
