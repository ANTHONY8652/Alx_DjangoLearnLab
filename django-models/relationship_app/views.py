from django.shortcuts import render, redirect
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from .models import Book, Library, UserProfile
from .forms import RegisterForm

# Function-based view to list books
@login_required
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view to display library details
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

# User registration view
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user, role='Member')
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'relationship_app/register.html', {'form': form})

# Admin view
@user_passes_test(lambda u: u.userprofile.role == 'Admin')
@login_required
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

# Librarian view
@user_passes_test(lambda u: u.userprofile.role == 'Librarian')
@login_required
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

# Member view
@user_passes_test(lambda u: u.userprofile.role == 'Member')
@login_required
def member_view(request):
    return render(request, 'relationship_app/member_view.html')
