from django.db import models


class BlogsArticle(models.Model):
    title = models.CharField(max_length=150, null=False, blank=False)
    text = models.TextField(null=False, blank=False)
    time = models.DateField()
    photo = models.ImageField(upload_to='media', default='photo.jpg')


class Comments(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    text = models.TextField(null=False, blank=False)
