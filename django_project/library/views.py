from django.shortcuts import render
from django.http import HttpResponse
from library.models import *

# Create your views here.
def index(request):
	#return HttpResponse("Hello, world. You're at the library index!")
	lib1 = Library.objects.all()
	return HttpResponse(lib1)
