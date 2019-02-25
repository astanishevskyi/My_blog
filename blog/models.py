from django.db import models
from datetime import datetime


class Article(models.Model):
    author = models.CharField(max_length=24, null=False, blank=False)
    text = models.TextField(null=False, blank=False)
    title = models.CharField(max_length=100, null=False, blank=False)
    # description = '%100s' % str(text)
    # time = models.DateTimeField(datetime.now(), default='2000-01-01')

    # def __str__(self):
    #     return self.title
