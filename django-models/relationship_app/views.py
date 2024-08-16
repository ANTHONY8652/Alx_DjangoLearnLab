from django.shortcuts import render
from .models import Book, Library
from django.views.generic.detail import DetailView

#Lists all books stored in tehe database
def list_books(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'list_books.html', context)

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'

# Create your views here.
