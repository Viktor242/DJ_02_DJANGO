from django.db import models

# Create your models here.

class News_post(models.Model):
    title = models.CharField('Название новости', max_length=50)
    short_description = models.CharField('Краткое описание новости', max_length=200)
    text = models.TextField('Новость')
    author = models.CharField('Автор новости', max_length=100)
    pub_date = models.DateTimeField('Дата публикации')

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'