from django.utils import timezone
from django.db import models

# Create your models here.
class BaseModel(models.Model):
    created_date = models.DateTimeField(verbose_name="Created date", editable=False)
    modified_date = models.DateTimeField(verbose_name="Modification Date")
    
    class Meta:
        abstract = True

class League(BaseModel):
    league_pk = models.AutoField(
        db_column="league_pk", 
        primary_key=True,
        verbose_name="Primary key of the table",
        help_text="Primary key of the table")
    
    league_id = models.BigIntegerField(
        verbose_name="Id League", 
        unique=True,
        null=False, 
        blank=False,
        help_text="Id League"
    )

    league_name = models.CharField(
        max_length=255, 
        verbose_name="League name", 
        null=False, 
        blank=False,
        help_text="Name of the league"
    )

    league_slug = models.SlugField(
        max_length=255, 
        verbose_name="Slug", 
        null=False, 
        blank=False,
        help_text="Slug of the league"
    )

    league_sport = models.CharField(
        max_length=6, 
        verbose_name="Sport", 
        null=False, 
        blank=False,
        help_text="Sport of the league"
    )

    league_image = models.SlugField(
        max_length=500, 
        verbose_name="Image of the league", 
        null=False, 
        blank=False,
        help_text="Image of the league"
    )

    league_light_image = models.ImageField(
        max_length=255, 
        verbose_name="Light Image", 
        null=False, 
        blank=False,
        help_text="Light Image of the league"
    )

    league_dark_image = models.ImageField(
        max_length=255, 
        verbose_name="Dark Image of the league", 
        null=False, 
        blank=False,
        help_text="Dark Image of the league"
    )

    league_region = models.CharField(
        max_length=255, 
        verbose_name="Region", 
        null=False, 
        blank=False,
        help_text="Region of the league"
    )

    league_priority = models.IntegerField(
        verbose_name="Priority", 
        default=0,
        help_text="Priority of the league"
    )

    league_display_priority_position = models.IntegerField(
        verbose_name="Display priority position", 
        null=False, 
        blank=False,
        help_text="Display priority position"
    )

    league_display_priority_status = models.BooleanField(
        verbose_name="Display Priority Status", 
        null=False, 
        blank=False,
        help_text="Display priority status"
    )

    class meta:
        db_table = "league"

    def save(self, *args, **kwargs):
        """ On save, update timestamps """
        if not self.league_pk:
            self.created_date = timezone.now()
        self.modified_date = timezone.now()
        return super(League, self).save(*args, **kwargs)

class Tournament(BaseModel):
    tournament_pk = models.AutoField(
        db_column="tournament_pk", 
        primary_key=True,
        verbose_name="Primary key of the table",
        help_text="Primary key of the table")
    tournament_id = models.BigIntegerField(unique=True,verbose_name="Tournament Id", help_text="Tournament ForeignKey")
    tournament_name = models.CharField(
        verbose_name="Name", max_length=255, null=False, blank=False, help_text="Tournament name"
    )
    tournament_slug = models.SlugField(
        verbose_name="Slug", max_length=255, null=False, blank=False, help_text="Tournament slug"
    )
    tournament_sport = models.CharField(
        verbose_name="Sport", max_length=255, null=False, blank=False, help_text="Tournament sport"
    )
    tournament_start_date = models.DateField(verbose_name="Start Date", null=False, blank=False, help_text="Tournament start date")
    tournament_end_date = models.DateField(verbose_name="End Date", null=False, blank=False, help_text="Tournament end date")

    class meta:
        db_table = "tournament"

    def save(self, *args, **kwargs):
        """ On save, update timestamps """
        if not self.tournament_pk:
            self.created_date = timezone.now()
        self.modified_date = timezone.now()
        return super(Tournament, self).save(*args, **kwargs)



class Team(BaseModel):
    team_pk = models.AutoField(
        db_column="team_pk", 
        primary_key=True,
        verbose_name="Primary key of the table",
        help_text="Primary key of the table")

    team_id = models.BigIntegerField(verbose_name="Team", unique=True, null=False, blank=False, help_text="Team ForeignKey")

    team_name = models.CharField(
        verbose_name="Name", max_length=255, null=False, blank=False, help_text="Team name"
    )
    team_acronym = models.CharField(
        verbose_name="Acronym", max_length=255, null=False, blank=False, help_text="Team acronym"
    )
    team_slug = models.SlugField(
        verbose_name="Slug", max_length=255, null=False, blank=False, help_text="Team slug"
    )

    class meta:
        db_table = "team"

    def save(self, *args, **kwargs):
        """ On save, update timestamps """
        if not self.team_pk:
            self.created_date = timezone.now()
        self.modified_date = timezone.now()
        return super(Team, self).save(*args, **kwargs)



class Player(BaseModel):
    player_pk = models.AutoField(
        db_column="player_pk", 
        primary_key=True,
        verbose_name="Primary key of the table",
        help_text="Primary key of the table")

    player_id = models.BigIntegerField(verbose_name="Player", unique=True, null=False, blank=False, help_text="Player identifier")

    team_id = models.BigIntegerField(verbose_name="Team", null=True, blank=True, help_text="Team ForeignKey")

    player_handle = models.CharField(
        verbose_name="Handle", max_length=16, null=False, blank=False, help_text="Player handle"
    )

    player_name = models.CharField(
        verbose_name="Name", max_length=255, null=False, blank=False, help_text="Player name"
    )

    class meta:
        db_table = "player"

    def save(self, *args, **kwargs):
        """ On save, update timestamps """
        if not self.player_pk:
            self.created_date = timezone.now()
        self.modified_date = timezone.now()
        return super(Player, self).save(*args, **kwargs)



class Game(BaseModel):
    game_pk = models.AutoField(
        db_column="game_pk", 
        primary_key=True,
        verbose_name="Primary key of the table",
        help_text="Primary key of the table")

    game_id = models.BigIntegerField(
        verbose_name="Game", null=False, blank=False, unique=True, help_text="Game identifier"
    )
    game_platform_id = models.CharField(
        verbose_name="Platform", max_length=255, null=False, blank=False, help_text="Game plataform identifier"
    )
    game_year = models.IntegerField(verbose_name="Year", null=False, blank=False, help_text="Game year")

    class meta:
        db_table = "game"

    def save(self, *args, **kwargs):
        """ On save, update timestamps """
        if not self.game_pk:
            self.created_date = timezone.now()
        self.modified_date = timezone.now()
        return super(Game, self).save(*args, **kwargs)



class GameDetail(BaseModel):
    game_detail_pk = models.AutoField(
        db_column="game_detail_pk", 
        primary_key=True,
        verbose_name="Primary key of the table",
        help_text="Primary key of the table")

    game_id = models.ForeignKey(
        Game,
        db_column="game_id",
        verbose_name="Game",
        null=False,
        blank=False,
        help_text="Game identifier",
        on_delete=models.CASCADE,
    )
    player_id = models.BigIntegerField(
        db_column="player_id", verbose_name="Player", null=False, blank=False, help_text="Player identifier"
    )
    game_detail_player_match = models.BooleanField(
        verbose_name="Player equal to player table",
        null=False,
        blank=False,
        default=False,
        help_text="Player match with the player table?"
    )

    class meta:
        db_table = "game_detail"

    def save(self, *args, **kwargs):
        """ On save, update timestamps """
        if not self.game_detail_pk:
            self.created_date = timezone.now()
        self.modified_date = timezone.now()
        return super(GameDetail, self).save(*args, **kwargs)



class Stage(BaseModel):
    stage_pk = models.AutoField(
        db_column="stage_pk", 
        primary_key=True,
        verbose_name="Primary key of the table",
        help_text="Primary key of the table")

    tournament_id = models.ForeignKey(
        Tournament,
        db_column="tournament_id",
        verbose_name="Tournament",
        null=True,
        help_text="Tournament ForeignKey",
        on_delete=models.CASCADE,
    )
    stage_name = models.CharField(
        verbose_name="Stage", max_length=255, null=False, blank=False, help_text="Stage name"
    )
    stage_type = models.CharField(verbose_name="Type", max_length=255, blank=True , null=True, help_text="Stage type")
    stage_slug = models.CharField(
        verbose_name="Slug", max_length=255, null=False, blank=False, help_text="Stage slug"
    )

    class meta:
        db_table = "stage"

    def save(self, *args, **kwargs):
        """ On save, update timestamps """
        if not self.stage_pk:
            self.created_date = timezone.now()
        self.modified_date = timezone.now()
        return super(Stage, self).save(*args, **kwargs)



class Section(BaseModel):
    section_pk = models.AutoField(
        db_column="section_pk", 
        primary_key=True,
        verbose_name="Primary key of the table",
        help_text="Primary key of the table")

    stage_id = models.ForeignKey(
        Stage, db_column="stage_pk", verbose_name="Stage", on_delete=models.CASCADE, help_text="Stage ForeignKey"
    )

    section_name = models.CharField(
        verbose_name="Section", max_length=255, null=False, blank=False, help_text="Section name"
    )

    class meta:
        db_table = "section"

    def save(self, *args, **kwargs):
        """ On save, update timestamps """
        if not self.section_pk:
            self.created_date = timezone.now()
        self.modified_date = timezone.now()
        return super(Section, self).save(*args, **kwargs)



class Match(BaseModel):
    match_pk = models.AutoField(
        db_column="match_pk", 
        primary_key=True,
        verbose_name="Primary key of the table",
        help_text="Primary key of the table")

    section_id = models.ForeignKey(
        Section, db_column="section_pk", verbose_name="Section Detail", on_delete=models.CASCADE, help_text="Section ForeignKey"
    )
    match_type = models.CharField(
        verbose_name="Type", max_length=255, null=False, blank=False, help_text="Match type"
    )
    match_state = models.CharField(
        verbose_name="State", max_length=255, null=False, blank=False, help_text="Match state"
    )
    match_mode = models.CharField(
        verbose_name="Mode", max_length=255, null=False, blank=False, help_text="Match mode"
    )
    match_strategy = models.CharField(
        verbose_name="Strategy", max_length=255, null=False, blank=False, help_text="Match strategy"
    )

    class meta:
        db_table = "match"

    def save(self, *args, **kwargs):
        """ On save, update timestamps """
        if not self.match_pk:
            self.created_date = timezone.now()
        self.modified_date = timezone.now()
        return super(Match, self).save(*args, **kwargs)



class MatchDetail(BaseModel):
    match_detail_pk = models.AutoField(
        db_column="match_detail_pk", 
        primary_key=True,
        verbose_name="Primary key of the table",
        help_text="Primary key of the table")

    match_id = models.ForeignKey(
        Match, verbose_name="Match", on_delete=models.CASCADE, help_text="Match ForeignKey")

    team_id = models.ForeignKey(Team, verbose_name="Team", on_delete=models.CASCADE, help_text="Team identifier")

    match_detail_match_team_integrant = models.BooleanField(
        verbose_name="Match Integrant", default=False, null=False, help_text="Match team integrants with integrants table?"
    )

    match_detail_win = models.BooleanField(verbose_name="Win Game?", null=False, blank=False, help_text="Win the game?")

    class meta:
        db_table = "match_detail"

    def save(self, *args, **kwargs):
        """ On save, update timestamps """
        if not self.match_detail_pk:
            self.created_date = timezone.now()
        self.modified_date = timezone.now()
        return super(MatchDetail, self).save(*args, **kwargs)


