from django.shortcuts import render
from django.http import HttpResponse
from library.models import *
from django.db.models import Q
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

def home(request):
    books = Books.objects.all()
    search_t = ''
    if 'search' in request.GET:
        search_t = request.GET['search']
        books = books.filter(title_icontaints=search_t)
        
        
    context = {
        'books': books,
        'search_t': search_t
        }
    
    return render(request, 'search/home.html,')

def search(request):
    query = request.GET.get('q', '')
    if query:
        queryset = (Q(title_icontaints=query))|(Q(author_icontains=query))
        results = Posts.objects.filter(queryset).distinct()
    else:
        results = []
    return render(request, 'search.html', context={'results': results, 'query': query})
