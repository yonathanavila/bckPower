from django.db import models


# Create your models here.
class League(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True)
    league_id = models.BigIntegerField(verbose_name="League", null=False, blank=False)
    league_name = models.CharField(
        max_length=255, verbose_name="Name", null=False, blank=False
    )
    league_slug = models.SlugField(
        max_length=255, verbose_name="Slug", null=False, blank=False
    )
    league_sport = models.CharField(
        max_length=6, verbose_name="Sport", null=False, blank=False
    )
    league_image = models.SlugField(
        max_length=500, verbose_name="Image", null=False, blank=False
    )
    league_light_image = models.ImageField(
        max_length=255, verbose_name="Light Image", null=False, blank=False
    )
    league_dark_image = models.ImageField(
        max_length=255, verbose_name="Dark Image", null=False, blank=False
    )
    league_region = models.CharField(
        max_length=255, verbose_name="Region", null=False, blank=False
    )
    league_priority = models.IntegerField(verbose_name="Priority", default=0)
    league_display_priority_position = models.IntegerField(
        verbose_name="Display Priority Position", null=False, blank=False
    )
    league_display_priority_status = models.BooleanField(
        verbose_name="Display Priority Status", null=False, blank=False
    )

    class meta:
        db_table = "league"


class Tournament(models.Model):
    tournament_id = models.BigIntegerField(primary_key=True, verbose_name="Id")
    league_id = models.BigIntegerField(verbose_name="League", null=False, blank=False)
    league_name = models.CharField(
        verbose_name="Name", max_length=255, null=False, blank=False
    )
    league_slug = models.SlugField(
        verbose_name="Slug", max_length=255, null=False, blank=False
    )
    league_sport = models.CharField(
        verbose_name="Sport", max_length=255, null=False, blank=False
    )
    league_start_date = models.DateField(verbose_name="Start Date", null=False, blank=False)
    league_end_date = models.DateField(verbose_name="End Date", null=False, blank=False)

    class meta:
        db_table = "tournament"


class Team(models.Model):
    team_id = models.BigIntegerField(
        primary_key=True, verbose_name="Team", null=False, blank=False
    )
    team_name = models.CharField(
        verbose_name="Name", max_length=255, null=False, blank=False
    )
    team_acronym = models.CharField(
        verbose_name="Acronym", max_length=255, null=False, blank=False
    )
    team_slug = models.SlugField(
        verbose_name="Slug", max_length=255, null=False, blank=False
    )

    class meta:
        db_table = "team"


class Player(models.Model):
    player_id = models.BigIntegerField(
        primary_key=True, verbose_name="Player", null=False, blank=False
    )
    player_team = models.BigIntegerField(verbose_name="Team", null=False, blank=False)
    player_handle = models.CharField(
        verbose_name="Handle", max_length=16, null=False, blank=False
    )
    player_name = models.CharField(
        verbose_name="Name", max_length=255, null=False, blank=False
    )

    class meta:
        db_table = "player"


class Game(models.Model):
    game_id = models.BigIntegerField(
        verbose_name="Game", primary_key=True, null=False, blank=False
    )
    game_platform_id = models.CharField(
        verbose_name="Platform", max_length=255, null=False, blank=False
    )
    game_year = models.IntegerField(verbose_name="Year", default=2023)

    class meta:
        db_table = "game"


class GameDetail(models.Model):
    game_id = models.ForeignKey(
        Game,
        db_column="game_id",
        verbose_name="Game",
        null=False,
        blank=False,
        on_delete=models.CASCADE,
    )
    player_id = models.BigIntegerField(
        db_column="player_id", verbose_name="Player", null=False, blank=False
    )
    player_match = models.BooleanField(
        verbose_name="Player equal to player table",
        null=False,
        blank=False,
        default=True,
    )

    class meta:
        db_table = "game_detail"


class Stage(models.Model):
    tournament_id = models.ForeignKey(
        Tournament,
        db_column="tournament_id",
        verbose_name="Tournament",
        null=True,
        on_delete=models.DO_NOTHING,
    )
    stage_name = models.CharField(
        verbose_name="Stage", max_length=255, null=False, blank=False
    )
    stage_type = models.CharField(verbose_name="Type", max_length=255, blank=True, null=True)
    stage_slug = models.CharField(
        verbose_name="Slug", max_length=255, null=False, blank=False
    )

    class meta:
        db_table = "stage"


class Section(models.Model):
    stage_id = models.ForeignKey(
        Stage, db_column="stage_id", verbose_name="Stage", on_delete=models.DO_NOTHING
    )
    section_name = models.CharField(
        verbose_name="Section", max_length=255, null=False, blank=False
    )

    class meta:
        db_table = "section"


class Match(models.Model):
    section_id = models.ForeignKey(
        Section, db_column="section_id", verbose_name="Section Detail", on_delete=models.DO_NOTHING
    )
    match_type = models.CharField(
        verbose_name="Type", max_length=255, null=False, blank=False
    )
    match_state = models.CharField(
        verbose_name="State", max_length=255, null=False, blank=False
    )
    match_mode = models.CharField(
        verbose_name="Mode", max_length=255, null=False, blank=False
    )
    match_strategy = models.CharField(
        verbose_name="Strategy", max_length=255, null=False, blank=False
    )

    class meta:
        db_table = "match"


class MatchDetail(models.Model):
    match_detail_id = models.ForeignKey(
        Match, db_column="match_detail_id", verbose_name="Match", on_delete=models.DO_NOTHING
    )
    team_id = models.ForeignKey(Team, db_column="team_id", verbose_name="Team", on_delete=models.DO_NOTHING)
    match_detail_match_team_integrant = models.BooleanField(
        verbose_name="Match Integrant", default=False, null=False
    )
    match_win = models.BooleanField(verbose_name="Win Game?", null=False, blank=False)

    class meta:
        db_table = "match_detail"
