# Generated by Django 4.1.2 on 2022-11-13 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_bet_date_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='bet',
            name='balance',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bet',
            name='date_created',
            field=models.DateTimeField(),
        ),
    ]
