# Generated by Django 4.2.1 on 2023-11-01 07:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('toDo', '0002_grouptasks_remove_task_status_task_iscomplete'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='isComplete',
        ),
    ]
