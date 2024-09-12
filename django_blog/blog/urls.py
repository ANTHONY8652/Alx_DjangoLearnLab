from django.urls import path, include
from .views import register, home

urlpatterns = [
    path('home/', home, name='home'),
    path('register/', register, name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
    ##path('register/', views.register, name='register'),
    #path('login/', views.user_login, name='login'),
    #path('logout/', views.user_logout, name='logout'),
    #path('profile/', views.profile, name='profile'),
]