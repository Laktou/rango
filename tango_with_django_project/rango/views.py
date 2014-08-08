from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponse

def index(request):
	context = RequestContext(request)
	context_dict = {'boldmessage': "I am bold font from the context"}
	return render_to_response('rango/index.html', context_dict, context)

def about(request):
	return HttpResponse("Rango says: Here is the about page. <a href='/rango/'>Main Page</a>")