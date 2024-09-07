from django.urls import path
from .views import DrinkList

urlpatterns = [
    path('api/drinks/', DrinkList.as_view(), name='drink-list'),
]