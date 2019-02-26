from django.db import models


class Article(models.Model):
    author = models.CharField(max_length=24, null=False, blank=False)
    text = models.TextField(null=False, blank=False)
    title = models.CharField(max_length=100, null=False, blank=False)
