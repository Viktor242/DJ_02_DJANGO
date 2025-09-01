#!/usr/bin/env python3
"""
URL configuration for zerocoder project.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),  # Подключаем URLs нашего приложения
]
