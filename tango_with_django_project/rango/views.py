from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponse

from rango.models import Category, Page
from rango.conversion import decode
def index(request):
	context = RequestContext(request)

	category_list = Category.objects.order_by('-likes')[:5]
	page_list = Page.objects.order_by('-views')[:5]
	context_dict = {'categories': category_list, 'pages': page_list}

	return render_to_response('rango/index.html', context_dict, context)

def about(request):
	context = RequestContext(request)
	context_dict = {'lizard': "a talking lizard"}
	return render_to_response('rango/about.html', context_dict, context)

def category(request, category_name_url):
	context = RequestContext(request)

	category_name = decode(category_name_url)
	context_dict = {'category_name': category_name}

	try:
		category = Category.objects.get(name=category_name)

		pages = Page.objects.filter(category=category)

		context_dict['pages'] = pages
		context_dict['category'] = category

	except Category.DoesNotExist:
		pass

	return render_to_response('rango/category.html', context_dict, context)