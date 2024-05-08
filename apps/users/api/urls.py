from django.urls import path
from .views import UserListCreateAPIView, UserRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('users/all/', UserListCreateAPIView.as_view(),
         name='api_users_list_create'),
    path('users/<int:pk>', UserRetrieveUpdateDestroyAPIView.as_view(),
         name='api_user_retrieve_update_destroy')
]
