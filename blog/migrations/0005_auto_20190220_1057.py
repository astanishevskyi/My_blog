# Generated by Django 2.1.5 on 2019-02-20 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20190220_1055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='description',
            field=models.TextField(blank=True, default='<django.db.models.fields.TextField>%200s', max_length=1000),
        ),
    ]