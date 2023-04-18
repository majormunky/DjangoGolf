from django.db import models
from django.contrib.auth import get_user_model


class GolfCourse(models.Model):
    HOLE_CHOICES = (
        ("9", "9 Holes"),
        ("18", "18 Holes"),
    )
    name = models.CharField(max_length=128)
    hole_count = models.CharField(
        max_length=64, choices=HOLE_CHOICES, default=HOLE_CHOICES[0][0]
    )
    tee_time_link = models.URLField(blank=True)
    website_link = models.URLField(blank=True)
    city = models.CharField(max_length=128, blank=True)
    state = models.CharField(max_length=128, blank=True)
    zip_code = models.CharField(max_length=128, blank=True)


class Hole(models.Model):
    name = models.CharField(max_length=64)
    nickname = models.CharField(max_length=128, blank=True)
    par = models.IntegerField(default=3)
    course = models.ForeignKey(GolfCourse, on_delete=models.CASCADE)


class Tee(models.Model):
    name = models.CharField(max_length=64)
    distance = models.CharField(max_length=10)
    hole = models.ForeignKey(Hole, on_delete=models.CASCADE)


class Game(models.Model):
    HOLE_CHOICES = (
        ("9", "9 Holes"),
        ("18", "18 Holes"),
    )
    date_played = models.DateTimeField()
    course = models.ForeignKey(GolfCourse, on_delete=models.CASCADE)
    holes_played = models.CharField(
        max_length=64, choices=HOLE_CHOICES, default=HOLE_CHOICES[0][0]
    )
    players = models.ManyToManyField(get_user_model(), through="UserGameLink")


class UserGameLink(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)


class HoleScore(models.Model):
    hole = models.ForeignKey(Hole, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    game = models.ForeignKey(UserGameLink, on_delete=models.CASCADE)
