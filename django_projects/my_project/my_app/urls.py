from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookListCreateAPIView, BookViewSet,CommentViewSet

router = DefaultRouter()
router.register(r'Book', BookViewSet)
router.register(r'Comment', CommentViewSet)
urlpatterns = [
    path('api/books/', BookListCreateAPIView.as_view(), name="book-list-create"),
    path('apiii/', include(router.urls)),
]