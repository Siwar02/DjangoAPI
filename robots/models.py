from django.db import models
from authentication.models import User
# Create your models here.

class Robot(models.Model):

    name = models.TextField()
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    

    class Meta:
        ordering: ['-updated_at']

    def __str__(self):
        return str(self.owner)+'s robot'