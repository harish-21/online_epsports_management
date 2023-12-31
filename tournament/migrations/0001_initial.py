# Generated by Django 4.0.1 on 2022-03-29 03:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('creater', '0001_initial'),
        ('player', '0002_remove_player_email_player_player_email_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='tournament',
            fields=[
                ('tournament_id', models.AutoField(primary_key=True, serialize=False)),
                ('tournament_name', models.CharField(max_length=20, unique=True)),
                ('game', models.CharField(max_length=20)),
                ('winner_prize', models.IntegerField(default=0)),
                ('runner_prize', models.IntegerField(default=0)),
                ('entry_fee', models.IntegerField(default=0)),
                ('organiser_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='creater.organiser')),
            ],
        ),
        migrations.CreateModel(
            name='matchs',
            fields=[
                ('match_id', models.AutoField(primary_key=True, serialize=False)),
                ('date_time', models.DateTimeField(unique=True)),
                ('team1_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='team1', to='player.team')),
                ('team2_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='player.team')),
                ('tournament_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tournament.tournament')),
            ],
        ),
    ]
