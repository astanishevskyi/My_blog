# Generated by Django 2.1.5 on 2019-02-20 20:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20190220_2051'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='description',
        ),
    ]