import pytest
from django.shortcuts import reverse
from rest_framework.test import APIClient
from rest_framework import status
from home import models


@pytest.mark.django_db
def test_can_add_player(normal_user):
    player_endpoint = reverse("api:players-list")
    client = APIClient()
    client.force_authenticate(user=normal_user)

    data = {
        "name": "Test Player"
    }

    res = client.post(player_endpoint, data)
    assert res.status_code == status.HTTP_200_OK
    assert res.data["name"] == data["name"]


@pytest.mark.django_db
def test_cant_see_other_users_players(normal_user, second_user):
    player_endpoint = reverse("api:players-list")
    client = APIClient()
    client.force_authenticate(user=normal_user)

    player_name = "First Player User"

    models.Player.objects.create(
        name="Second User Player",
        added_by=second_user
    )

    models.Player.objects.create(
        name=player_name,
        added_by=normal_user
    )

    player_list = client.get(player_endpoint)
    assert len(player_list.data) == 1
    assert player_list.data[0]["name"] == player_name


@pytest.mark.django_db
def test_create_game_works(normal_user, golf_course):
    game_endpoint = reverse("api:game-list")
    client = APIClient()
    client.force_authenticate(user=normal_user)

    data = {
        "course": golf_course.id,
        "holes_played": golf_course.hole_count
    }

    res = client.post(game_endpoint, data)
    assert res.status_code == status.HTTP_200_OK
