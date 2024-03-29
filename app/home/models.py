from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

HOLE_CHOICES = (
    ("9", "9 Holes"),
    ("18", "18 Holes"),
)


class GolfCourse(models.Model):
    name = models.CharField(max_length=128)
    hole_count = models.CharField(
        max_length=64, choices=HOLE_CHOICES, default=HOLE_CHOICES[0][0]
    )
    tee_time_link = models.URLField(blank=True)
    website_link = models.URLField(blank=True)
    city = models.CharField(max_length=128, blank=True)
    state = models.CharField(max_length=128, blank=True)
    zip_code = models.CharField(max_length=128, blank=True)

    def __str__(self):
        return self.name


class Hole(models.Model):
    name = models.CharField(max_length=64)
    nickname = models.CharField(max_length=128, blank=True)
    par = models.IntegerField(default=3)
    order = models.IntegerField(default=0)
    course = models.ForeignKey(GolfCourse, on_delete=models.CASCADE)


class Tee(models.Model):
    name = models.CharField(max_length=64)
    distance = models.CharField(max_length=10)
    hole = models.ForeignKey(Hole, on_delete=models.CASCADE)


class Game(models.Model):
    STATUS_CHOICES = (
        ("setup", "Setup"),
        ("active", "Active"),
        ("completed", "Completed"),
        ("not_finished", "Not Finished"),
    )
    date_played = models.DateTimeField(blank=True, null=True)
    course = models.ForeignKey(GolfCourse, on_delete=models.CASCADE)
    holes_played = models.CharField(
        max_length=64, choices=HOLE_CHOICES, default=HOLE_CHOICES[0][0]
    )
    status = models.CharField(
        max_length=64, choices=STATUS_CHOICES, default=STATUS_CHOICES[0][0]
    )
    players = models.ManyToManyField("Player", through="PlayerGameLink")
    league_game = models.BooleanField(default=False)

    def start(self):
        self.status = "active"
        self.date_played = timezone.now()
        self.save()


class PlayerGameLink(models.Model):
    player = models.ForeignKey("Player", on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)


class HoleScore(models.Model):
    hole = models.ForeignKey(Hole, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    game = models.ForeignKey(PlayerGameLink, on_delete=models.CASCADE)


class Player(models.Model):
    name = models.CharField(max_length=64)
    user_account = models.OneToOneField(
        get_user_model(), on_delete=models.CASCADE, blank=True, null=True
    )
    added_by = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name="added_by"
    )

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ["name", "added_by"]


class TeeTime(models.Model):
    course = models.ForeignKey(GolfCourse, on_delete=models.CASCADE)
    tee_time = models.DateTimeField()
    players = models.ManyToManyField("Player")
    holes_to_play = models.CharField(
        max_length=64, choices=HOLE_CHOICES, default=HOLE_CHOICES[0][0]
    )
    is_active = models.BooleanField(default=True)
