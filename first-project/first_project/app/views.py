import os

from django.http import HttpResponse
from django.shortcuts import render, reverse
import datetime


def home_view(request):
    template_name = 'app/home.html'

    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }

    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    now = datetime.datetime.now()
    msg = f'Текущее время: {now.strftime("%d-%m-%Y %H:%M:%S")}'
    return HttpResponse(msg)


def workdir_view(request):
    files_list = os.listdir()
    message = f"Список файлов в директории:{files_list}"
    return HttpResponse(message)

