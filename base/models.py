from django.db import models


# Create your models here.
class League(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True)
    idLeague = models.BigIntegerField(verbose_name="League", null=False, blank=False)
    name = models.CharField(
        max_length=255, verbose_name="Name", null=False, blank=False
    )
    slug = models.SlugField(
        max_length=255, verbose_name="Slug", null=False, blank=False
    )
    sport = models.CharField(
        max_length=6, verbose_name="Sport", null=False, blank=False
    )
    image = models.SlugField(
        max_length=500, verbose_name="Image", null=False, blank=False
    )
    lightImage = models.ImageField(
        max_length=255, verbose_name="Light Image", null=False, blank=False
    )
    darkImage = models.ImageField(
        max_length=255, verbose_name="Dark Image", null=False, blank=False
    )
    region = models.CharField(
        max_length=255, verbose_name="Region", null=False, blank=False
    )
    priority = models.IntegerField(verbose_name="Priority", default=0)
    displayPriorityPosition = models.IntegerField(
        verbose_name="Display Priority Position", null=False, blank=False
    )
    displayPriorityStatus = models.BooleanField(
        verbose_name="Display Priority Status", null=False, blank=False
    )

    class meta:
        db_table = "league"


class Tournament(models.Model):
    idTournament = models.BigIntegerField(primary_key=True, verbose_name="Id")
    idLeague = models.BigIntegerField(verbose_name="League", null=False, blank=False)
    name = models.CharField(
        verbose_name="Name", max_length=255, null=False, blank=False
    )
    slug = models.SlugField(
        verbose_name="Slug", max_length=255, null=False, blank=False
    )
    sport = models.CharField(
        verbose_name="Sport", max_length=255, null=False, blank=False
    )
    startDate = models.DateField(verbose_name="Start Date", null=False, blank=False)
    endDate = models.DateField(verbose_name="End Date", null=False, blank=False)

    class meta:
        db_table = "tournament"


class Team(models.Model):
    idTeam = models.BigIntegerField(
        primary_key=True, verbose_name="Team", null=False, blank=False
    )
    name = models.CharField(
        verbose_name="Name", max_length=255, null=False, blank=False
    )
    acronym = models.CharField(
        verbose_name="Acronym", max_length=255, null=False, blank=False
    )
    slug = models.SlugField(
        verbose_name="Slug", max_length=255, null=False, blank=False
    )

    class meta:
        db_table = "team"


class Player(models.Model):
    idPlayer = models.BigIntegerField(
        primary_key=True, verbose_name="Player", null=False, blank=False
    )
    idTeam = models.BigIntegerField(verbose_name="Team", null=False, blank=False)
    handle = models.CharField(
        verbose_name="Handle", max_length=16, null=False, blank=False
    )
    name = models.CharField(
        verbose_name="Name", max_length=255, null=False, blank=False
    )

    class meta:
        db_table = "player"


class Game(models.Model):
    idGame = models.BigIntegerField(
        verbose_name="Game", primary_key=True, null=False, blank=False
    )
    idPlatform = models.CharField(
        verbose_name="Platform", max_length=255, null=False, blank=False
    )
    year = models.IntegerField(verbose_name="Year", default=2023)

    class meta:
        db_table = "game"


class GameDetail(models.Model):
    idGame = models.ForeignKey(
        Game,
        db_column="idGame",
        verbose_name="Game",
        null=False,
        blank=False,
        on_delete=models.CASCADE,
    )
    idPlayer = models.BigIntegerField(
        db_column="IdPlayer", verbose_name="Player", null=False, blank=False
    )
    playerMatch = models.BooleanField(
        verbose_name="Player equal to player table",
        null=False,
        blank=False,
        default=True,
    )

    class meta:
        db_table = "gameDetail"


class Stage(models.Model):
    idTournament = models.ForeignKey(
        Tournament,
        db_column="idTournament",
        verbose_name="Tournament",
        null=True,
        on_delete=models.DO_NOTHING,
    )
    name = models.CharField(
        verbose_name="Stage", max_length=255, null=False, blank=False
    )
    type = models.CharField(verbose_name="Type", max_length=255, blank=True, null=True)
    slug = models.CharField(
        verbose_name="Slug", max_length=255, null=False, blank=False
    )

    class meta:
        db_table = "stage"


class Section(models.Model):
    idStage = models.ForeignKey(
        Stage, db_column="idStage", verbose_name="Stage", on_delete=models.DO_NOTHING
    )
    name = models.CharField(
        verbose_name="Section", max_length=255, null=False, blank=False
    )

    class meta:
        db_table = "section"


class Match(models.Model):
    idSection = models.ForeignKey(
        Section, db_column="idSection", verbose_name="Section Detail", on_delete=models.DO_NOTHING
    )
    type = models.CharField(
        verbose_name="Type", max_length=255, null=False, blank=False
    )
    state = models.CharField(
        verbose_name="State", max_length=255, null=False, blank=False
    )
    mode = models.CharField(
        verbose_name="Mode", max_length=255, null=False, blank=False
    )
    strategy = models.CharField(
        verbose_name="Strategy", max_length=255, null=False, blank=False
    )

    class meta:
        db_table = "match"


class MatchDetail(models.Model):
    idMatch = models.ForeignKey(
        Match, db_column="idMatch", verbose_name="Match", on_delete=models.DO_NOTHING
    )
    idTeam = models.ForeignKey(Team, db_column="idTeam", verbose_name="Team", on_delete=models.DO_NOTHING)
    matchTeamIntegrants = models.BooleanField(
        verbose_name="Match Integrants", default=False, null=False
    )
    win = models.BooleanField(verbose_name="Win Game?", null=False, blank=False)

    class meta:
        db_table = "matchDetail"
