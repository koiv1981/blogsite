from django.db import models
from django.urls import reverse_lazy

"""
Caregory 
=============
title, slug 

Tag
=============
title, slug 

Post
============= 
title, slug, author, contetnt, created_at, photo, views, category, tags

Subscribe
============
email, created_at

Comment
============
post, name, email, content, creared_at, updated_at, is_published
"""


class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название категории')
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy('category', kwargs={'slug': self.slug})

    class Meta:
        ordering = ["title"]
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Tag(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название тэга')
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy('tag', kwargs={"slug": self.slug})

    class Meta:
        ordering = ["title"]
        verbose_name = "Тэг"
        verbose_name_plural = "Тэги"


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название поста')
    slug = models.SlugField(max_length=255, unique=True)
    author = models.CharField(max_length=255, verbose_name='Автор поста')
    content = models.TextField(blank=True, verbose_name='Содержание поста')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Опубликовано")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True, verbose_name='Изображение')
    views = models.IntegerField(default=0, verbose_name="Кол-во просмотров")
    category = models.ForeignKey("Category", on_delete=models.PROTECT, related_name="posts", verbose_name='Категория')
    tags = models.ManyToManyField("Tag", blank=True, related_name='posts', verbose_name='Тэг')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy('post', kwargs={"slug": self.slug})

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Пост"
        verbose_name_plural = "Посты"


class Subscriber(models.Model):
    email = models.EmailField(max_length=50, verbose_name='email', unique=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата подписки")

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Подписчик"
        verbose_name_plural = "Подписчики"


class Comment(models.Model):
    post = models.ForeignKey("Post", on_delete=models.PROTECT, related_name='comments', verbose_name="Пост")
    name = models.CharField(max_length=80, verbose_name="Имя")
    email = models.EmailField(verbose_name="Адрес электронной почты")
    content = models.TextField(verbose_name="Содержание комментария")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создан")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Обновлен")
    is_published = models.BooleanField(default=True, verbose_name="Опубликован")

    # def get_absolute_url(self):
    #     return reverse_lazy('add_comment', kwargs={"comment_id": self.pk})

    class Meta:
        ordering = ["created_at"]
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"


    def __str__(self):
        return f'{self.post}'