# Generated by Django 4.2 on 2023-07-11 14:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("home", "0021_alter_player_unique_together"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="player",
            unique_together=set(),
        ),
        migrations.AlterField(
            model_name="player",
            name="added_by",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="added_by",
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
    ]