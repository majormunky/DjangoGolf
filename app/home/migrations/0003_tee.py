# Generated by Django 4.2 on 2023-04-18 00:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0002_hole"),
    ]

    operations = [
        migrations.CreateModel(
            name="Tee",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=64)),
                ("distance", models.CharField(max_length=10)),
                (
                    "hole",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="home.hole"
                    ),
                ),
            ],
        ),
    ]