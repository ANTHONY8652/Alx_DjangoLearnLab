from django.urls import path, include
from .views import drink_list, DrinkList
from omudrink import views
#from rest_framework import DefaultRouter
from .views import DrinkViewSet

#router = DefaultRouter()
#router.register=(r"Drink", DrinkViewSet)

urlpatterns = [
    ##path('router/', include(router.urls)),
    path('api/', DrinkList.as_view(), name='drink-list'),
    path('tutorial/', views.drink_list),
]