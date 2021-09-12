from django.shortcuts import render
from catalog.models import Book, Author, BookInstance, Genre #importa as classes
from django.views import generic

# Create your views here.
def index(request):
    """View function for home page of site"""

    #Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    #Available books (status = a)
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    #the 'all()' is implied by default
    num_authors = Author.objects.count()

    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_visits': num_visits,
    }

    #Render the HTML template index.html with data in the context variable
    return render(request, 'index.html', context=context)

class BookListView(generic.ListView):
    model = Book #view genérica consulta no banco de dados o modelo

class BookDetailView(generic.DetailView):
    model = Book

class AuthorView(generic.ListView):
    model = Author

class AuthorDetailView(generic.DetailView):
    model = Author