#!/usr/bin/env python3
from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Category


def index(request):
    """Главная страница"""
    context = {
        'title': 'Главная страница - Мой блог о котиках'
    }
    return render(request, 'main/index.html', context)


def about(request):
    """Страница о нас"""
    context = {
        'title': 'О нас - Мой блог о котиках'
    }
    return render(request, 'main/about.html', context)





def help(request):
    """Страница помощи"""
    context = {
        'title': 'Помощь'
    }
    return render(request, 'main/help.html', context)


def kotiki(request):
    """Страница с котиками"""
    context = {
        'title': 'Котики'
    }
    return render(request, 'main/kotiki.html', context)
