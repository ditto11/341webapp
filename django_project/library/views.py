from django.shortcuts import render
from django.http import HttpResponse
from library.models import *
from django.db.models import Q
from django.views.decorators.cache import never_cache
from django.view.generic import TemplateView, ListView

# Create your views here.
@never_cache
#def index(request):
	#return HttpResponse("Hello, world. You're at the library index!")
#	books = Book.objects.filter(author="Tamora Pierce")
#	htmlString = """<title>Library Database Search</title> <body> """
#	for word in books:
#		htmlString = htmlString + "<br>" + word.title
#	htmlString += "</body>"
#	return HttpResponse(htmlString)

class SearchView(ListView):
        model = Book
        template_name = 'search.html'
        
#class HomePageView(TemplateView):
    #template_name = 'home.html'

def home(request):
    books = Book.objects.all()
    search_t = ''
    if 'search' in request.GET:
       search_t = request.GET['search']
       books = Book.objects.filter(title__icontains=search_t)
        
        
   # context = {
       # 'books': books,
       # 'search_t': search_t
       # }
    
    return render(request, 'home.html')

def get_queryset(self):
    query = self.request.GET.get('q')
    object_list = Book.objects.filter(
        Q(title_icontains=query | Q(author_icontains=query)
)
        return object_list

#def search(request):
   # books = Book.objects.all()
   # query = request.GET.get("q")
   # if query:
       # books = books.filter(Q(title__icontains=query))|(Q(author__icontains=query)).distinct()
        #return render(request, 'search.html', {'books':books})
   # else:
        #return render(request, 'search.html', {'books': books })
#