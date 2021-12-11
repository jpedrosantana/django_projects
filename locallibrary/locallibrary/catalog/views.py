from django.shortcuts import redirect, render, get_object_or_404
from catalog.models import Book, Author, BookInstance, Genre #importa as classes
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from django.contrib.auth import login
from django.contrib import messages
from .forms import CreateBookForm, NewUserForm, RenewBookForm

import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import permission_required

from django.views.generic.edit import CreateView, UpdateView, DeleteView


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

    num_genres = Genre.objects.all().count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_visits': num_visits,
        'num_genres': num_genres,
    }

    #Render the HTML template index.html with data in the context variable
    return render(request, 'index.html', context=context)

def register_requests(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("index")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request = request, template_name='register.html', context={'register_form': form})

class BookListView(generic.ListView):
    #Listas genéricas procura por model_name_list.html
    model = Book #view genérica consulta no banco de dados o modelo
    paginate_by = 10

class BookDetailView(generic.DetailView):
    model = Book

class AuthorView(generic.ListView):
    model = Author

class AuthorDetailView(generic.DetailView):
    model = Author

class LoanedBooksByUserListView(LoginRequiredMixin, generic.ListView):
    """Generic class-based view listing books on loan to current user"""
    model = BookInstance
    template_name = 'catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 10

    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')

class BorrowedListView(PermissionRequiredMixin, generic.ListView):
    permission_required = 'catalog.can_mark_returned'
    model = BookInstance
    template_name = 'catalog/borrowed_list.html'

@permission_required('catalog.can_mark_returned')
def renew_book_librarian(request, pk):
    book_instance = get_object_or_404(BookInstance, pk=pk)

    if request.method == 'POST':
        #create a form instance and populate it wit data from the request (binding)
        form = RenewBookForm(request.POST)

        if form.is_valid():
            #process the data as required
            book_instance.due_back = form.cleaned_data['due_back']
            book_instance.save()

            #redirect to an specific page (initial page in this case)
            return HttpResponseRedirect(reverse('borrowed'))
    #if this is a GET or other method, create the default form
    else:
        proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
        form = RenewBookForm(initial={'due_back': proposed_renewal_date})

    context = {
        'form': form,
        'book_instance': book_instance
    }

    return render(request, 'catalog/book_renew_librarian.html', context)


class AuthorCreate(PermissionRequiredMixin, CreateView):
    permission_required = 'catalog.can_mark_returned'
    model = Author
    fields = '__all__'
    initial = {'date_of_death': '05/01/2018'}

class AuthorUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = 'catalog.can_mark_returned'
    model = Author
    fields = ['first_name', 'last_name', 'date_of_birth', 'date_of_death']

class AuthorDelete(PermissionRequiredMixin, DeleteView):
    #view Delete espera encontrar um arquivo de confirmação modelname_confirm_delete.html
    permission_required = 'catalog.can_mark_returned'
    model = Author
    success_url = reverse_lazy('authors')

class BookCreate(PermissionRequiredMixin, CreateView):
    permission_required = 'catalog.can_mark_returned'
    model = Book
    form_class = CreateBookForm
    template_name='catalog/book_form.html'
    success_url = reverse_lazy('books')

class BookUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = 'catalog.can_mark_returned'
    model = Book
    fields = ['title', 
            'author',
            'summary',
            'isbn',
            'genre',]

class BookDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'catalog.can_mark_returned'
    model = Book
    success_url = reverse_lazy('books')

    