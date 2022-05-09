from django.urls import path
from . import views


urlpatterns = [
    path('', views.RobotListAPIView.as_view(), name="robots"),
    path('<int:id>', views.RobotDetailAPIView.as_view(), name="robots"),
]