from django.db import models

class GroupTasks(models.Model):
    title = models.CharField(max_length=255)
# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=255)
    priority = models.IntegerField()
    time_create = models.TimeField(auto_now_add=True)
    time_complete = models.TimeField()
    
    def __str__(self) -> str:
        return self.title


    class Meta:
        ordering = ['-priority', 'time_create']


