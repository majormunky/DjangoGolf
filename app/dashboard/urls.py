from django.urls import path
from . import views

app_name = "dashboard"

urlpatterns = [
    path("", views.index, name="index"),
    path("courses/", views.course_list, name="courses"),
    path("courses/add/", views.add_course, name="add_course"),
]
