# Generated by Django 2.1.5 on 2019-02-27 16:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serviceworksnames',
            name='service_name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.Service'),
        ),
        migrations.AlterField(
            model_name='specialserviceworksnames',
            name='service_name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.SpecialService'),
        ),
    ]
