from django.urls import path
from . import views


urlpatterns = [
    path('', views.UserListAPIView.as_view(), name="users"),
    path('<int:id>', views.UserDetailAPIView.as_view(), name="user"),
]