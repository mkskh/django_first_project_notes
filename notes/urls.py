from django.urls import path
from . import views


app_name = 'notes_app'

urlpatterns = [
    path('notes/', views.welcome, name='welcome'),
    path('notes/section/', views.section, name='section'),
    path('notes/section/<str:part_name>/', views.get_part, name="get_part"),
    path('notes/<int:note_number>/', views.notes_navigation, name="notes_navigation"),
    path('notes/<str:string>/', views.match_web, name="match_web"),
    path('<int:note_number>/', views.redirect_to_notes, name='redirect_to_notes'),
]