from django.urls import path
from .views import *

urlpatterns = [
    path("users/",UserListCreateView.as_view(), name="user_list_create"),
    path("users/<int:user_id>/",UserDetailUpdateDeleteView.as_view(),name="user_detail_update_delete"),
]
