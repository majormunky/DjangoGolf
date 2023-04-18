# Generated by Django 4.2 on 2023-04-18 03:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("home", "0009_playergamelink_game_players_holescore_game"),
    ]

    operations = [
        migrations.AlterField(
            model_name="player",
            name="user_account",
            field=models.OneToOneField(
                blank=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]