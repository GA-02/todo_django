from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import json
from toDo.models import Task

@login_required
def tasksUser(request):
    tasks = Task.objects.all()
    
    tasks = tasks.filter(user = request.user)
    data = []
    for task in tasks:
        data.append({'userName': task.user.username, 'title': task.title})
    data2 = json.dumps(data)
    return  HttpResponse(data, content_type='application/json')

# Create your views here.
