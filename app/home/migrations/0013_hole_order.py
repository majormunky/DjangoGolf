# Generated by Django 4.2 on 2023-04-20 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0012_game_status"),
    ]

    operations = [
        migrations.AddField(
            model_name="hole",
            name="order",
            field=models.IntegerField(default=0),
        ),
    ]
