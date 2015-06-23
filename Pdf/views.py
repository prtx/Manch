from django.shortcuts import render
from django.http import HttpResponseRedirect ,HttpResponse

# Create your views here.

def show(request):
	return HttpResponse(open('static/pythondevmeet.pdf'),content_type='application/pdf')
