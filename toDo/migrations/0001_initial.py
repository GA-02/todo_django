# Generated by Django 4.2.1 on 2023-11-01 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('priority', models.IntegerField()),
                ('status', models.BooleanField()),
                ('time_create', models.TimeField(auto_now_add=True)),
                ('time_complete', models.TimeField()),
            ],
            options={
                'ordering': ['-priority', 'time_create'],
            },
        ),
    ]
