# Generated by Django 3.1.2 on 2020-11-12 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20201107_1119'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='line',
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Face', 'Face'), ('Lips', 'Lips'), ('Eyes', 'Eyes')], max_length=10),
        ),
    ]
