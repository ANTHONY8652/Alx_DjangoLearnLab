from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Post, Book
from django.http import HttpResponse
from .forms import BookForm

@permission_required('bookshelf.can_add_book')
def add_book(request):
    if request.method == "POST":
        form = BookForm(request.Post)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
        return render(request, 'bookshelf/add_book.html', {'form': form})
    
@permission_required('bookshelf.can_delete_book')
def delete_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == "POST":
        book.delete()
        return redirect('book_list')
    return render(request, 'bookshelf/delete_book.html', {'book': book})

def index(request):
    return HttpResponse("First site")

@permission_required('bookshelf.can_view', raise_exception=True)
def view_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'bookshelf/view_pots.html', {'post': post})

@permission_required('bookshelf.can_create', raise_exception=True)
def create_post(request):
    if request.method == "POST":
        pass
    return render(request, 'bookshelf/create_post.html')

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == "POST":
        pass
    return render(request, 'bookshelf/edit_post', {'post': post})

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == "POST":
        post.delete()
    return redirect('bookshelf:post_list')


# Create your views here.
