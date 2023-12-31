# Generated by Django 4.0.1 on 2022-03-29 02:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='team',
            fields=[
                ('team_id', models.AutoField(primary_key=True, serialize=False)),
                ('team_name', models.CharField(max_length=20)),
                ('game', models.CharField(max_length=20)),
                ('no_players', models.IntegerField()),
                ('points', models.IntegerField(default=0)),
                ('wins', models.IntegerField(default=0)),
                ('losses', models.IntegerField(default=0)),
                ('draws', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='player',
            fields=[
                ('player_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('player_score', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('no_of_matchs', models.IntegerField()),
                ('team_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='player.team')),
            ],
        ),
    ]
