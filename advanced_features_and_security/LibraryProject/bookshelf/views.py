from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Post
from django.http import HttpResponse

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
