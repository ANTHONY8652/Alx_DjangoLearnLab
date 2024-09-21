from django.urls import path
from .views import NotificationViewSet

urlpattersn = [
    path('', NotificationViewSet.as_view({'get': 'list'}), name='user-notifications'),
]