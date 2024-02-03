from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from .models import Note


def welcome(request):
    section_url = reverse('notes:section')
    return HttpResponse(f'<h1>Welcome to my course notes!</h1>\
                        <a href="{section_url}">Check the list of section</a>')

def get_part(request, part_name):
    section_url = reverse('notes:section')
    parts = {
        "Web_Frameworks": f'<h1>Notes about Web Frameworks</h1><ol>\
            <li>Web frameworks are a way to improve our productivity and make complex things look easy.</li>\
            <li>Django is a web framework written with Python that offers a "batteries included" approach, as \
            opposed to Flask, that aims at minimizing the initial features to reduce the footprint.</li>\
            <li>Most web frameworks use the MVC design pattern that states that logic, data and visualization \
            should be kept in different places.</li></ol><a href="{section_url}">Back to sections</a>',
        "URL_Mapping": f'<h1>Notes about URL Mapping</h1><ol>\
            <li>URL Mapping can be very easy at the beginning but it may become extremely complex in some cases.</li>\
            <li>URL endpoints may be defined with literals and parameters, which will be passed on to the view.</li>\
            <li>Parameters passed with the > and < will be passed as keyword arguments. Back to sections.</li></ol>\
            <a href="{section_url}">Back to sections</a>',
        "Setting_up_Django": f'<h1>Notes about Setting up Django</h1><ol>\
            <li>Setting up Django is very simple. It requires installing Django, starting project and an app.</li>\
            <li>The staftproject command lets us specify the directory where the project will be created.</li>\
            <li>Django comes with a development web server that makes it very simple to install and start working.</li></ol>\
            <a href="{section_url}">Back to sections</a>'
    }
    part = parts[part_name]
    return HttpResponse(part)


def section(request):
    welcome_url = reverse('notes:welcome')
    get_part_one = reverse('notes:get_part', args=['Web_Frameworks'])
    get_part_two = reverse('notes:get_part', args=['URL_Mapping'])
    get_part_three = reverse('notes:get_part', args=['Setting_up_Django'])
    return HttpResponse(f'<h1>Browse my notes by section</h1><ol><li><a href="{get_part_one}">Web Frameworks</a></li>\
                        <li><a href="{get_part_two}">URL Mapping</a></li><li><a href="{get_part_three}">Setting up Django\
                        </a></li></ol><a href="{welcome_url}">Back to home</a>') 




def match_web(request, string):

    welcome_url = reverse('notes:welcome')

    notes = Note.objects.all()

    matched = []

    for dict in notes:
        if string.lower() in dict.text.lower():
            matched.append(f"<li>{dict.text}</li>")

    return HttpResponse(f'<h1>Notes matching {string}</h1><ol>{"".join([line for line in matched])}</ol>\
                        <a href="{welcome_url}">Back to home</a>')


def notes_navigation(request, note_number):
    pass
