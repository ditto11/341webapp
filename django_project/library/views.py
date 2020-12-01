from django.shortcuts import render
from django.http import HttpResponse
from library.models import *
from django.views.decorators.cache import never_cache

# Create your views here.
@never_cache
def index(request):
	#return HttpResponse("Hello, world. You're at the library index!")
	books = Book.objects.filter(author="Tamora Pierce")
	htmlString = """<title>Library Database Search</title> <body> """
	for word in books:
		htmlString = htmlString + "<br>" + word.title
	htmlString += "</body>"
	return HttpResponse(htmlString)
