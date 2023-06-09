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
    assert res.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db
def test_add_player_to_game_works(normal_user, golf_game, player):
    add_player_endpoint = reverse("api:game-add_player", args=[golf_game.id])

    client = APIClient()
    client.force_authenticate(user=normal_user)

    data = {
        "player": player.id
    }

    res = client.post(add_player_endpoint, data)
    assert res.status_code == status.HTTP_200_OK

    golf_game.refresh_from_db()
    assert player in golf_game.players.all()


@pytest.mark.django_db
def test_remove_player_from_game_works(normal_user, golf_game_with_player):
    player = golf_game_with_player.players.all().first()
    remove_player_endpoint = reverse("api:game-remove_player", args=[golf_game_with_player.id])
    data = {
        "player": player.id
    }
    client = APIClient()
    client.force_authenticate(user=normal_user)

    res = client.post(remove_player_endpoint, data)
    assert res.status_code == status.HTTP_200_OK

    golf_game_with_player.refresh_from_db()

    assert golf_game_with_player.players.count() == 0
    assert player not in golf_game_with_player.players.all()


@pytest.mark.django_db
def test_add_player_to_game_with_no_player_returns_error(normal_user, golf_game, player):
    add_player_endpoint = reverse("api:game-add_player", args=[golf_game.id])

    client = APIClient()
    client.force_authenticate(user=normal_user)

    data = {}

    res = client.post(add_player_endpoint, data)
    assert res.status_code == status.HTTP_404_NOT_FOUND
