from django.urls import path
from . import views
from .views import PostCreateView, PostDeleteView, PostDetailView, PostListView, PostUpdateView


urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('profile/', views.profile_view, name='profile'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('postlist/', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name=
         'post-create'),
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post-update-view'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete-view'),
]