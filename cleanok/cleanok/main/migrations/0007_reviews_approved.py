# Generated by Django 2.1.5 on 2019-03-03 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20190228_0417'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviews',
            name='approved',
            field=models.BooleanField(default=False, verbose_name='Одобрен'),
        ),
    ]
