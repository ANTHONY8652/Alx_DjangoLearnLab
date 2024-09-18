from django.urls import path
from . import views
from .views import PostCreateView, PostDeleteView, PostDetailView, PostListView, PostUpdateView, CommentCreateView, CommentDeleteView, CommentUpdateView, search_view
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    ##Authentication urls
    path('register/', views.register_view, name='register'),
    path('profile/', views.profile_view, name='profile'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    ##Post urls
    path('postlist/', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name=
         'post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update-view'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete-view'),
    ##Comment urls
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='comment_create'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment_edit'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete'),
    ##TAg and search
    path('tags/<slug:tag>/', views.tagged_posts, name='posts_by_tag'),
    path('search/', search_view, name='search'),
    path('tags/<slug:tag_slug>/', views.PostByTagListView.as_view(), name='posts_by_tag'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)