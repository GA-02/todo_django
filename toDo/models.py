from django.contrib.auth.models import User
from django.db import models

class GroupTasks(models.Model):
    title = models.CharField(max_length=255)

class Task(models.Model):
    title = models.CharField(max_length=255)
    priority = models.IntegerField()
    time_create = models.TimeField(auto_now_add=True)
    time_complete = models.TimeField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    def __str__(self) -> str:
        return self.title


    class Meta:
        ordering = ['-priority', 'time_create']


