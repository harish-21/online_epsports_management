# Generated by Django 4.0.1 on 2022-05-05 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matchs', '0004_matchs_winner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matchs',
            name='date_time',
            field=models.DateField(),
        ),
    ]
