from django.db import models
from django.conf import settings


class Article(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None)
    text = models.TextField(null=False, blank=False)
    title = models.CharField(max_length=100, null=False, blank=False)


class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None)
    text = models.TextField(null=False, blank=False)
    
