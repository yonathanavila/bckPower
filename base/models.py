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


class Tournament(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True, verbose_name="Id")
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


class Team(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True, verbose_name="Id")
    idTeam = models.BigIntegerField(verbose_name="Team", null=False, blank=False)
    name = models.CharField(
        verbose_name="Name", max_length=255, null=False, blank=False
    )
    acronym = models.CharField(
        verbose_name="Acronym", max_length=255, null=False, blank=False
    )
    slug = models.SlugField(
        verbose_name="Slug", max_length=255, null=False, blank=False
    )


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


class Game(models.Model):
    idGame = models.BigIntegerField(
        verbose_name="Game", primary_key=True, null=False, blank=False
    )
    idPlatform = models.CharField(
        verbose_name="Platform", max_length=255, null=False, blank=False
    )
    year = models.IntegerField(verbose_name="Year", default=2023)


class GameDetail(models.Model):
    idGameDetail = models.IntegerField(primary_key=True,verbose_name="GameDetail", auto_created=True)
    idGame = models.ForeignKey(
        Game,
        db_column="IdGame",
        verbose_name="Game",
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        unique=False,
    )
    idPlayer = models.ForeignKey(
        Player,
        db_column="IdPlayer",
        verbose_name="Player",
        on_delete=models.CASCADE,
        null=False,
        blank=False
    )
    playerMatch = models.BooleanField(
        verbose_name="Player equal to player table",
        null=False,
        blank=False,
        default=True
    )

    class meta:
        db_table = "base_game_detail"
