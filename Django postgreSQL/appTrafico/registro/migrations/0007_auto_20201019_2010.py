# Generated by Django 3.1.2 on 2020-10-19 23:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0006_auto_20201019_2009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensor_dato',
            name='presion',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(880), django.core.validators.MaxValueValidator(1080)]),
        ),
    ]
