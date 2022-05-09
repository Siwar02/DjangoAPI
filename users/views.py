from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import UsersSerializer
from .models import Users
from rest_framework import permissions

from authentication.models import User
# Create your views here.
class UserListAPIView(ListCreateAPIView):
    serializer_class = UsersSerializer
    queryset = User.objects.all()


class UserDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = UsersSerializer
    queryset = User.objects.all()
    lookup_field = "id"
