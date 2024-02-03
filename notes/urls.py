from django.urls import path
from . import views


app_name = 'notes_app'

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('section/', views.section, name='section'),
    path('section/<str:part_name>/', views.get_part, name="get_part"),
    path('<str:string>/', views.match_web, name="match_web"),
    path('<int:note_number>/', views.notes_navigation, name="notes_navigation"),
]