# Generated by Django 3.1.2 on 2020-11-07 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20201030_1638'),
    ]

    operations = [
        # migrations.RemoveField(
        #     model_name='product',
        #     name='ingredients',
        # ),
        # migrations.RemoveField(
        #     model_name='product',
        #     name='line',
        # ),
        migrations.RemoveField(
            model_name='product',
            name='lineDescription',
        ),
        migrations.AlterField(
            model_name='product',
            name='additionalImages',
            field=models.FileField(blank=True, upload_to='additional'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Lips', 'Lips'), ('Face', 'Face'), ('Eyes', 'Eyes')], max_length=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.FileField(upload_to='products'),
        ),
    ]
