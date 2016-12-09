from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render

from . import forms


def home_page(request):
	return render(request, 'home.html')

def flight_view(request):
	#form = forms.home_page()
	if request.method == 'POST':
		#form = forms.home_page(request.POST)
		#if form.is_valid():
		print(request.POST.get("destination"))
	return render(request, 'home.html')



def contact_page(request):
	return render(request, 'contact.html')





