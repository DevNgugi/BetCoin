# Generated by Django 4.1.2 on 2022-11-08 05:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_bet_progression_alter_bet_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bet',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 8, 8, 25, 32, 645143)),
        ),
    ]
