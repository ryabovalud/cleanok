# Generated by Django 2.1.5 on 2019-02-27 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20190228_0300'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviews',
            name='reviewer_photo',
            field=models.ImageField(default='', upload_to='static/images/review'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='whywe',
            name='image_for_description',
            field=models.ImageField(default='', upload_to='static/images/whywe/description'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='whywe',
            name='image_for_name',
            field=models.ImageField(default='', upload_to='static/images/whywe/name'),
            preserve_default=False,
        ),
    ]
