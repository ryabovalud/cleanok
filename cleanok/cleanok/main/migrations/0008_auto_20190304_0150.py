# Generated by Django 2.1.5 on 2019-03-03 15:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_reviews_approved'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reviews',
            name='reviewer_photo',
        ),
        migrations.RemoveField(
            model_name='whywe',
            name='image_for_description',
        ),
        migrations.RemoveField(
            model_name='whywe',
            name='image_for_name',
        ),
    ]
