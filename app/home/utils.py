from home import models


def get_players_for_game(user, game):
    return models.Player.objects.filter(
        added_by=user
    ).exclude(
        game__in=[game.id]
    )


def get_holes_for_game(course, holes_to_play):
    hole_list = models.Hole.objects.filter(course=course).order_by("order")

    if course.hole_count == holes_to_play:
        return hole_list

    if course.hole_count == "18" and holes_to_play == "front-9":
        return hole_list.filter(order__gte=1, order__lt=10)

    if course.hole_count == "18" and holes_to_play == "back-9":
        return hole_list.filter(order__gte=10)

    return None


def create_hole_scores_for_game(game, holes_to_play):
    """
    holes_to_play might be:
        - 9
        - front-9
        - back-9
        - 18
    """
    hole_list = get_holes_for_game(game.course, holes_to_play)
    if hole_list is None:
        return False

    for hole in hole_list:
        for player in game.players.all():
            game_link = models.PlayerGameLink.objects.filter(
                player=player, game=game
            ).first()
            hole_score = models.HoleScore(hole=hole, game=game_link)
            hole_score.save()
