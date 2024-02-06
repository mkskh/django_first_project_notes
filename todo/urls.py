from django.urls import path
from . import views


app_name = 'todo_app'

urlpatterns = [
    path('<int:todo_number>/', views.todo_navigation, name='todo_navigation'),

]