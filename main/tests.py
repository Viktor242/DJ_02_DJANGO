#!/usr/bin/env python3
from django.test import TestCase
from django.urls import reverse
from .models import Post, Category


class PostModelTest(TestCase):
    """Тесты для модели Post"""
    
    def setUp(self):
        """Настройка тестовых данных"""
        self.post = Post.objects.create(
            title="Тестовый пост",
            content="Содержание тестового поста"
        )
    
    def test_post_creation(self):
        """Тест создания поста"""
        self.assertEqual(self.post.title, "Тестовый пост")
        self.assertEqual(self.post.content, "Содержание тестового поста")
        self.assertIsNotNone(self.post.created_at)
    
    def test_post_str_method(self):
        """Тест строкового представления поста"""
        self.assertEqual(str(self.post), "Тестовый пост")


class MainViewsTest(TestCase):
    """Тесты для представлений"""
    
    def setUp(self):
        """Настройка тестовых данных"""
        self.post = Post.objects.create(
            title="Тестовый пост",
            content="Содержание тестового поста"
        )
    
    def test_index_view(self):
        """Тест главной страницы"""
        response = self.client.get(reverse('main:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Тестовый пост")
    
    def test_post_detail_view(self):
        """Тест детальной страницы поста"""
        response = self.client.get(reverse('main:post_detail', args=[self.post.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Тестовый пост")
