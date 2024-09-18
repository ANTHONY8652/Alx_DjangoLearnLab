from django.urls import path
from .views import RegisterUser, LoginUser, FollowUserView, UnfollowUserView

urlpatterns = [
    ##REgistration and login urls
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    ##Followers and unfollowing views
    path('follow/<int:user_id>/', FollowUserView.as_view(), name='follower_usa'),
    path('unfollow/<int:user_id>/', UnfollowUserView.as_view(), name='unfollowusa'),
]