from typing import Any
from django.core.management.base import BaseCommand
from todo.models import Todos


class Command(BaseCommand):
    help = 'Populate the database with notes'

    def handle(self, *args, **kwargs):
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

        for todo in todos: 
            Todos.objects.create(text=todo['text'], topic=todo['topic'], status=todo['status'])
            
        self.stdout.write(self.style.SUCCESS('Database populated successfully'))
