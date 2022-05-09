from rest_framework import serializers
from .models import Robot


class RobotsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Robot
        fields = ['id','name']
        