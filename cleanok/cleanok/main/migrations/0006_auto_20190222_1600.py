# Generated by Django 2.1.7 on 2019-02-22 16:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20190214_0300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specialserviceworksnames',
            name='service_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.SpecialService', to_field='name'),
        ),
    ]