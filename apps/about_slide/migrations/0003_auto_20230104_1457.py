# Generated by Django 3.2.7 on 2023-01-04 20:57

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about_slide', '0002_about_slide_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='about_slide_photo',
            name='image',
        ),
        migrations.AddField(
            model_name='about_slide_photo',
            name='file',
            field=cloudinary.models.CloudinaryField(default='', max_length=255),
        ),
    ]
