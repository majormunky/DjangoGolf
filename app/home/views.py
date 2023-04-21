from django.shortcuts import render
from home import models


def index(request):
    game_list = None
    if request.user.is_authenticated:
        game_list = models.Game.objects.filter(
            status="active", players__in=[request.user.player]
        )
    return render(request, "home/index.html", {"game_list": game_list})


def course_list(request):
    course_list = models.GolfCourse.objects.all().order_by("name")
    return render(request, "home/course_list.html", {"course_list": course_list})
