# Generated by Django 3.1.2 on 2021-01-06 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_category_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='image',
        ),
        migrations.AddField(
            model_name='category',
            name='banner',
            field=models.FileField(blank=True, default='', null=True, upload_to='categories/banner'),
        ),
        migrations.AddField(
            model_name='category',
            name='teaser',
            field=models.FileField(blank=True, default='', null=True, upload_to='categories/teaser'),
        ),
    ]
