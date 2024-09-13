from django.urls import path
from . import views
from .views import PostCreateView, PostDeleteView, PostDetailView, PostListView, PostUpdateView, CommentCreateView, CommentDeleteView, CommentUpdateView


urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('profile/', views.profile_view, name='profile'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('postlist/', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name=
         'post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update-view'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete-view'),
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='comment_create'),
    path('comments/<int:pk>/edit/', CommentUpdateView.as_view(), name='comment_edit'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete'),
]