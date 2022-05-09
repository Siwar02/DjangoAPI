from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import RobotsSerializer
from .models import Robot
from rest_framework import permissions
from .permissions import IsOwner
# Create your views here.
class RobotListAPIView(ListCreateAPIView):
    serializer_class = RobotsSerializer
    queryset = Robot.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)

class RobotDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = RobotsSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner,)
    queryset = Robot.objects.all()
    lookup_field = "id"

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)