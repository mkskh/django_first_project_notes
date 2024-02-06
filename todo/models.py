from django.db import models


todos = [
    {
        "text": "Start the repository",
        "topic": "Course Project",
        "status": "done"
    },
    {
        "text": "Set up Django",
        "topic": "Course Project",
        "status": "done"
    },
    {
        "text": "Read more about URLconf",
        "topic": "Lectures",
        "status": "done"
    },
    {
        "text": "Fix the cabinet",
        "topic": "Personal",
        "status": "done"
    },
    {
        "text": "Create forms",
        "topic": "Course Project",
        "status": "pending"
    },
]




class Todos(models.Model):
    text = models.TextField()
    topic = models.CharField(max_length=100)
    status = models.CharField(max_length=100)




# Commands for run:
# python manage.py makemigrations
# python manage.py migrate
