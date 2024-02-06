from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from .models import Todos


def todo_navigation(request, todo_number):
    get_previous = reverse('todo:todo_navigation', args=[todo_number - 1])
    get_next = reverse('todo:todo_navigation', args=[todo_number + 1])

    todo = get_object_or_404(Todos, id=todo_number)

    h2 = todo.topic
    text = todo.text
    status = todo.status

    if todo_number == 5: 
        response = HttpResponse(f'<h1>To Do number {todo_number}</h1><h2>{h2}</h2>\
                            <p>{text}</p><p>{status}</p><a href="{get_previous}">Previous note |</a> \
                            Next note')
    elif todo_number == 1:
        response = HttpResponse(f'<h1>To Do number {todo_number}</h1><h2>{h2}</h2>\
                            <p>{text}</p><p>{status}</p><p>Previous note |<a href="{get_next}"> Next note</a></p>')
    else:
        response = HttpResponse(f'<h1>To Do number {todo_number}</h1><h2>{h2}</h2>\
                            <p>{text}</p><p>{status}</p><a href="{get_previous}">Previous note |</a> \
                            <a href="{get_next}">Next note</a>')
    return response