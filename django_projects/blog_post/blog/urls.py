from django.urls import path
from .views import PostListCreateAPIView, PostRetrieveUpdateeDestroyAPIView
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt import TokenRefreshView

urlpatterns = [
    path('posts/', PostListCreateAPIView.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', PostRetrieveUpdateeDestroyAPIView.as_view(), name='post-retrieve-update-destroy'),
    path('api/token/', obtain_auth_token, name='api_token_obtain'),
    path('api/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
]