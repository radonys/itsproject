from django.shortcuts import render
from django.views import generic
# Create your views here.
class indexview(generic.ListView):
	template_name = 'restapi/index.html'
	
