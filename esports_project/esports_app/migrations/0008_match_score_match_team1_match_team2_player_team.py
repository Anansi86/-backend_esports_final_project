# Generated by Django 4.1.3 on 2022-12-03 23:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('esports_app', '0007_match_score_hero_player_matches'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='score',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='score', to='esports_app.match_score'),
        ),
        migrations.AddField(
            model_name='match',
            name='team1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Team1', to='esports_app.team'),
        ),
        migrations.AddField(
            model_name='match',
            name='team2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Team2', to='esports_app.team'),
        ),
        migrations.AddField(
            model_name='player',
            name='team',
            field=models.ManyToManyField(related_name='players', to='esports_app.team'),
        ),
    ]
