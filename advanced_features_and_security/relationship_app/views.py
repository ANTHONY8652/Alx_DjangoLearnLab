from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Library

def list_bookss(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

class library_detail_view(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')  # Redirect to a home page or other page after registration
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from .models import Book, Library

def is_admin(user):
    return user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.userprofile.role == 'Librarian'

def is_member(user):
    return user.userprofile.role == 'Member'

@user_passes_test(is_admin)
def admin_view(request):
    # Logic for the admin view
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(is_librarian)
def librarian_view(request):
    # Logic for the librarian view
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(is_member)
def member_view(request):
    # Logic for the member view
    return render(request, 'relationship_app/member_view.html')

def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

from django.views.generic import DetailView

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import permission_required
from .models import Books

@permission_required('relationship_app.can_add_book')
def add_book(request):
    pass

@permission_required('relationship_app.can_change_book')
def edit_book(request, book_id):
    pass

@permission_required('relationship_app.can_delete_book')
def delete_book(request, book_id):
    pass


