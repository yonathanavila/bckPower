import csv, json
from .models import (
    League,
    Tournament,
    Team,
    Player,
    Game,
    GameDetail,
    Stage,
    Section,
    Match,
    MatchDetail,
)
from django.http import HttpResponse, JsonResponse, Http404
from django.utils.decorators import method_decorator
from django.views import View
from django.db import transaction
from pathlib import Path
from .script import get_object_or_false

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = str(Path(__file__).resolve().parent.parent)

from .script import download_esports_files, download_games


def index(request):
    return HttpResponse("Hello World")


# Create your views here.
@transaction.atomic
def SetLeague(request):
    listLeagues = []
    dir = BASE_DIR + "/data/2021/esports-data/leagues.json"
    with open(dir) as f:
        reader = json.load(f)
        for row in reader:
            print(row)
            if not row["id"] in listLeagues:
                modelRow = League()
                modelRow.league_id = row["id"]
                modelRow.league_name = row["name"]
                modelRow.league_slug = row["slug"]
                modelRow.league_sport = row["sport"]
                modelRow.league_image = row["image"]
                modelRow.league_light_image = row["lightImage"]
                modelRow.league_dark_image = row["darkImage"]
                modelRow.league_region = row["region"]
                modelRow.league_priority = row["priority"]
                modelRow.league_display_priority_position = row["displayPriority"][
                    "position"
                ]
                modelRow.league_display_priority_status = (
                    True if row["displayPriority"]["status"] == "selected" else False
                )
                modelRow.save()
                listLeagues.append(row["id"])
    dir = BASE_DIR + "/data/2022/esports-data/leagues.json"
    with open(dir) as f:
        reader = json.load(f)
        for row in reader:
            print(row)
            if not row["id"] in listLeagues:
                modelRow = League()
                modelRow.league_id = row["id"]
                modelRow.league_name = row["name"]
                modelRow.league_slug = row["slug"]
                modelRow.league_sport = row["sport"]
                modelRow.league_image = row["image"]
                modelRow.league_light_image = row["lightImage"]
                modelRow.league_dark_image = row["darkImage"]
                modelRow.league_region = row["region"]
                modelRow.league_priority = row["priority"]
                modelRow.league_display_priority_position = row["displayPriority"][
                    "position"
                ]
                modelRow.league_display_priority_status = (
                    True if row["displayPriority"]["status"] == "selected" else False
                )
                modelRow.save()
                listLeagues.append(row["id"])

    dir = BASE_DIR + "/data/2023/esports-data/leagues.json"
    with open(dir) as f:
        reader = json.load(f)
        for row in reader:
            print(row)
            if not row["id"] in listLeagues:
                modelRow = League()
                modelRow.league_id = row["id"]
                modelRow.league_name = row["name"]
                modelRow.league_slug = row["slug"]
                modelRow.league_sport = row["sport"]
                modelRow.league_image = row["image"]
                modelRow.league_light_image = row["lightImage"]
                modelRow.league_dark_image = row["darkImage"]
                modelRow.league_region = row["region"]
                modelRow.league_priority = row["priority"]
                modelRow.league_display_priority_position = row["displayPriority"][
                    "position"
                ]
                modelRow.league_display_priority_status = (
                    True if row["displayPriority"]["status"] == "selected" else False
                )
                modelRow.save()
                listLeagues.append(row["id"])
    return JsonResponse(
        {"success": True, "message": "Data saved correctly!", "data": "Hello World"}
    )


@transaction.atomic
def getAllLeagues(request):
    result = League.objects.all()
    return HttpResponse(result)


@transaction.atomic
def SetTournaments(request):
    listTournaments = []
    dir = BASE_DIR + "/data/2023/esports-data/tournaments.json"
    with open(dir) as f:
        reader = json.load(f)
        for row in reader:
            if not row["id"] in listTournaments:
                modelRow = Tournament()
                modelRow.tournament_id = row["id"]
                modelRow.league_id = row["leagueId"]
                modelRow.tournament_name = row["name"]
                modelRow.tournament_slug = row["slug"]
                modelRow.tournament_sport = row["sport"]
                modelRow.tournament_start_date = row["startDate"]
                modelRow.tournament_end_date = row["endDate"]
                modelRow.save()
                listTournaments.append(row["id"])

    dir = BASE_DIR + "/data/2022/esports-data/tournaments.json"
    with open(dir) as f:
        reader = json.load(f)
        for row in reader:
            if not row["id"] in listTournaments:
                modelRow = Tournament()
                modelRow.tournament_id = row["id"]
                modelRow.league_id = row["leagueId"]
                modelRow.tournament_name = row["name"]
                modelRow.tournament_slug = row["slug"]
                modelRow.tournament_sport = row["sport"]
                modelRow.tournament_start_date = row["startDate"]
                modelRow.tournament_end_date = row["endDate"]
                modelRow.save()
                listTournaments.append(row["id"])

    dir = BASE_DIR + "/data/2021/esports-data/tournaments.json"
    with open(dir) as f:
        reader = json.load(f)
        for row in reader:
            if not row["id"] in listTournaments:
                modelRow = Tournament()
                modelRow.tournament_id = row["id"]
                modelRow.league_id = row["leagueId"]
                modelRow.tournament_name = row["name"]
                modelRow.tournament_slug = row["slug"]
                modelRow.tournament_sport = row["sport"]
                modelRow.tournament_start_date = row["startDate"]
                modelRow.tournament_end_date = row["endDate"]
                modelRow.save()
                listTournaments.append(row["id"])
    return HttpResponse("Data saved in Tournament table")


@transaction.atomic
def SetTeams(request):
    listTeams = []
    dir = BASE_DIR + "/data/2021/esports-data/teams.json"

    with open(dir) as f:
        reader = json.load(f)
        for row in reader:
            if not row["team_id"] in listTeams:
                modelRow = Team()
                modelRow.team_id = row["team_id"]
                modelRow.team_name = row["name"]
                modelRow.team_acronym = row["acronym"]
                modelRow.team_slug = row["slug"]
                modelRow.save()
                listTeams.append(row["team_id"])
    dir = BASE_DIR + "/data/2022/esports-data/teams.json"
    with open(dir) as f:
        reader = json.load(f)
        for row in reader:
            if not row["team_id"] in listTeams:
                modelRow = Team()
                modelRow.team_id = row["team_id"]
                modelRow.team_name = row["name"]
                modelRow.team_acronym = row["acronym"]
                modelRow.team_slug = row["slug"]
                modelRow.save()
                listTeams.append(row["team_id"])

    dir = BASE_DIR + "/data/2023/esports-data/teams.json"
    with open(dir) as f:
        reader = json.load(f)
        for row in reader:
            if not row["team_id"] in listTeams:
                modelRow = Team()
                modelRow.team_id = row["team_id"]
                modelRow.team_name = row["name"]
                modelRow.team_acronym = row["acronym"]
                modelRow.team_slug = row["slug"]
                modelRow.save()
                listTeams.append(row["team_id"])

    return HttpResponse("Data saved in Teams table")


@transaction.atomic
def SetPlayers(request):
    listPlayers = []
    dir = BASE_DIR + "/data/2022/esports-data/players.json"
    with open(dir) as f:
        reader = json.load(f)
        for row in reader:
            if not row["player_id"] in listPlayers:
                modelRow = Player()
                modelRow.player_id = row["player_id"]
                modelRow.team_id = row["home_team_id"] if row["home_team_id"] else None
                modelRow.player_handle = row["handle"]
                modelRow.player_name = str(row["first_name"] + " " + row["last_name"])
                modelRow.save()
                listPlayers.append(row["player_id"])

    dir = BASE_DIR + "/data/2021/esports-data/players.json"
    with open(dir) as f:
        reader = json.load(f)
        for row in reader:
            if not row["player_id"] in listPlayers:
                modelRow = Player()
                modelRow.player_id = row["player_id"]
                modelRow.team_id = row["home_team_id"] if row["home_team_id"] else None
                modelRow.player_handle = row["handle"]
                modelRow.player_name = str(row["first_name"] + " " + row["last_name"])
                modelRow.save()
                listPlayers.append(row["player_id"])
    dir = BASE_DIR + "/data/2023/esports-data/players.json"
    with open(dir) as f:
        reader = json.load(f)
        for row in reader:
            if not row["player_id"] in listPlayers:
                modelRow = Player()
                modelRow.player_id = row["player_id"]
                modelRow.team_id = row["home_team_id"] if row["home_team_id"] else None
                modelRow.player_handle = row["handle"]
                modelRow.player_name = str(row["first_name"] + " " + row["last_name"])
                modelRow.save()
                listPlayers.append(row["player_id"])
    return HttpResponse("Data saved in PLayers table")


class SetGame(View):
    def get(self, request):
        listGames = []
        try:
            dir = BASE_DIR + "/data/2023/esports-data/mapping_data.json"
            with open(dir) as f:
                reader = json.load(f)
                # READ the json file
                for gameNumber, row in enumerate(reader):
                    # if gameNumber > 20000 and gameNumber < 30000 and not row["esportsGameId"] in listGames:
                    if not row["esportsGameId"] in listGames:
                        with transaction.atomic():
                            # save into model game
                            gameModel = Game()
                            gameModel.game_id = row["esportsGameId"]
                            gameModel.game_platform_id = row["platformGameId"]
                            gameModel.game_year = 2023
                            gameModel.save()
                            listGames.append(row["esportsGameId"])
            print("Open 2022")

            dir = BASE_DIR + "/data/2022/esports-data/mapping_data.json"
            with open(dir) as f:
                reader = json.load(f)
                # READ the json file
                for gameNumber, row in enumerate(reader):
                    # if gameNumber > 20000 and gameNumber < 30000 and not row["esportsGameId"] in listGames:
                    if not row["esportsGameId"] in listGames:
                        with transaction.atomic():
                            # save into model game
                            gameModel = Game()
                            gameModel.game_id = row["esportsGameId"]
                            gameModel.game_platform_id = row["platformGameId"]
                            gameModel.game_year = 2023
                            gameModel.save()
                            listGames.append(row["esportsGameId"])

            dir = BASE_DIR + "/data/2021/esports-data/mapping_data.json"
            with open(dir) as f:
                reader = json.load(f)
                # READ the json file
                for gameNumber, row in enumerate(reader):
                    # if gameNumber > 20000 and gameNumber < 30000 and not row["esportsGameId"] in listGames:
                    if not row["esportsGameId"] in listGames:
                        with transaction.atomic():
                            # save into model game
                            gameModel = Game()
                            gameModel.game_id = row["esportsGameId"]
                            gameModel.game_platform_id = row["platformGameId"]
                            gameModel.game_year = 2023
                            gameModel.save()
                            listGames.append(row["esportsGameId"])

                            print("Save correct: ", row["esportsGameId"])
                            # listGames.append(row['esportsGameId']);
                            # listParticipants = row["participantMapping"];
                            # if self.validate_player_list(listParticipants):
                            # self.save_game_detail(row["esportsGameId"], listParticipants);
                            # else:
                            # print(
                            # "\nPlayer list isn't complete, quit current player list"
                            # )
        except Exception as e:
            print(str(e))
            return HttpResponse(str(e))
        return HttpResponse("Data saved correctly")


class SetGameDetail(View):
    def get(self, request):
        listGames = []
        try:
            with transaction.atomic():
                dir = BASE_DIR + "/data/2023/esports-data/mapping_data.json"
                with open(dir) as f:
                    reader = json.load(f)
                    # READ the json file
                    for gameNumber, row in enumerate(reader):
                        # if gameNumber > 20000 and gameNumber < 30000 and not row["esportsGameId"] in listGames:
                        if not row["esportsGameId"] in listGames:
                            with transaction.atomic():
                                # save into model game
                                listGames.append(row["esportsGameId"])
                                listParticipants = row["participantMapping"]
                                if self.validate_player_list(listParticipants):
                                    self.save_game_detail(
                                        row["esportsGameId"], listParticipants
                                    )
                                else:
                                    print(
                                        "\nPlayer list isn't complete, quit current player list"
                                    )
                                    print(listParticipants)

            print("Open 2022")

            dir = BASE_DIR + "/data/2022/esports-data/mapping_data.json"
            with open(dir) as f:
                reader = json.load(f)
                # READ the json file
                for gameNumber, row in enumerate(reader):
                    # if gameNumber > 20000 and gameNumber < 30000 and not row["esportsGameId"] in listGames:
                    if not row["esportsGameId"] in listGames:
                        with transaction.atomic():
                            # save into model game
                            listGames.append(row["esportsGameId"])
                            listParticipants = row["participantMapping"]
                            if self.validate_player_list(listParticipants):
                                self.save_game_detail(
                                    row["esportsGameId"], listParticipants
                                )
                            else:
                                print(
                                    "\nPlayer list isn't complete, quit current player list"
                                )
                                print(listParticipants)

            print("Open 2021")
            dir = BASE_DIR + "/data/2021/esports-data/mapping_data.json"
            with open(dir) as f:
                reader = json.load(f)
                # READ the json file
                for gameNumber, row in enumerate(reader):
                    # if gameNumber > 20000 and gameNumber < 30000 and not row["esportsGameId"] in listGames:
                    if not row["esportsGameId"] in listGames:
                        with transaction.atomic():
                            # save into model game
                            gameModel.game_id = row["esportsGameId"]
                            listGames.append(row["esportsGameId"])
                            if self.validate_player_list(listParticipants):
                                self.save_game_detail(
                                    row["esportsGameId"], listParticipants
                                )
                            else:
                                print(
                                    "\nPlayer list isn't complete, quit current player list"
                                )
                                print(listParticipants)
        # "\nPlayer list isn't complete, quit current player list"
        except Exception as e:
            return HttpResponse(str(e))
        return HttpResponse("Data saved correctly")

    def save_game_detail(self, game_id, listPlayers):
        try:
            playersFounded = []
            for player in listPlayers:
                # Get Player Id
                player_id = listPlayers[player]
                queryPlayer = self.get_object("Player", player_id)
                if queryPlayer:
                    gameDetail = {"player_id": player_id, "playerMatch": True}
                    playersFounded.append(gameDetail)
                else:
                    gameDetail = {"player_id": player_id, "playerMatch": False}
                    playersFounded.append(gameDetail)
            print("Game id to save as detail is: ", game_id)
            for playerFounded in playersFounded:
                with transaction.atomic():
                    print(playerFounded)
                    gameQuery = self.get_object("Game", game_id)
                    gameDetailInstace = GameDetail(
                        game_id=gameQuery,
                        player_id=playerFounded["player_id"],
                        game_detail_player_match=playerFounded["playerMatch"],
                    )
                    print(gameDetailInstace)
                    gameDetailInstace.save()
                    print("Game detail is saved!")
        except Exception as e:
            return JsonResponse({"message": "Wasn't save correctly", "success": False})

    def get_object(self, modelName, id):
        try:
            if modelName == "Player":
                return Player.objects.get(player_id=int(id))
            else:
                return Game.objects.get(game_id=int(id))
        except Player.DoesNotExist:
            return False

    def validate_player_list(self, players):
        listValidation = []
        try:
            for player in players:
                if not players[player].isdigit():
                    listValidation.append(False)
                else:
                    listValidation.append(True)

            if False in listValidation:
                return False
            else:
                if len(listValidation) == 10:
                    return True
                else:
                    return False
                listValidation.clear()
        except Exception as e:
            print("eRROR?", str(e))
            return JsonResponse({"message": "Wasn't save correctly", "success": False})


# save the stages from tournaments data
@method_decorator(transaction.atomic, name="dispatch")
class SetStagesAndSection(View):
    def get(self, request):
        listStages = []
        try:
            dir = BASE_DIR + "/data/2023/esports-data/tournaments.json"
            with open(dir) as f:
                tournaments = json.load(f)
                for tournament in tournaments:
                    queryset = get_object_or_false(
                        tournament["id"], Tournament, "primaryKey"
                    )
                    if not queryset:
                        print(
                            "\nSkip curret stage => idTournament #:" + tournament["id"]
                        )
                    else:
                        print(queryset)
                        stages = tournament["stages"]
                        for stage in stages:
                            ################
                            ## save stage ##
                            ################
                            model = Stage()
                            model.tournament_id = queryset
                            model.stage_name = stage["name"]
                            model.stage_type = stage["type"]
                            model.stage_slug = stage["slug"]
                            model.save()
                            # get last object
                            """ querysetLast = self.get_object_or_false(
                                stage["name"], Stage, "lastField"
                            ) """
                            ###################
                            ## save sections ##
                            ###################
                            sections = stage["sections"]
                            for section in sections:
                                modelSection = Section(
                                    stage_id=model, section_name=section["name"]
                                )

                                modelSection.save()

                                ################
                                ## save match ##
                                ################

                                matches = section["matches"]
                                for match in matches:
                                    modelMatch = Match(
                                        section_id=modelSection,
                                        match_type=match["type"],
                                        match_state=match["state"],
                                        match_mode=match["mode"],
                                        match_strategy=match["strategy"]["type"]
                                        + " "
                                        + str(match["strategy"]["count"]),
                                    )
                                    modelMatch.save()

                                    #######################
                                    ## save match detail ##
                                    #######################
                                    # get the list of teams in one game only two teams
                                    teams = match["teams"]
                                    # verify if the participant exist in player table

                                    for team in teams:
                                        players = team["players"]
                                        print(
                                            "Verifying this list of participants: ",
                                            players,
                                        )

                                        # get the player match
                                        matchPlayers = self.participants_match_or_false(
                                            players
                                        )
                                        # get the team model
                                        queryTeam = self.get_object_or_false(
                                            team["id"], Team, "primaryKey"
                                        )

                                        if not queryTeam:
                                            print(
                                                "\nSkip curret detail => team_id #:"
                                                + team["id"]
                                            )
                                        else:
                                            modelMatchDetail = MatchDetail(
                                                match_id=modelMatch,
                                                team_id=queryTeam,
                                                match_detail_match_team_integrant=matchPlayers,
                                                match_detail_win=False
                                                if team["result"]["outcome"] == "loss"
                                                else True,
                                            )
                                            modelMatchDetail.save()
            return JsonResponse(
                {"message": "Your information was save correctly", "success": True}
            )
        except Exception as e:
            print("ERROR: ", str(e))
            return JsonResponse({"message": "Wasn't save correctly", "success": False})

    def participants_match_or_false(self, listIntegrants):
        listMatches = []
        try:
            for integrant in listIntegrants:
                print("Verifying player #: ", integrant["id"])
                response = Player.objects.get(player_id=integrant["id"])
                listMatches.append(response)

            if False in listMatches:
                return False
            else:
                return True
        except Exception as e:
            return False

    def get_object_or_false(self, key, model, type):
        try:
            if type == "primaryKey":
                return model.objects.get(team_id=key)
            if type == "lastField":
                return model.objects.last()
            else:
                return model.objects.get(name=key)
        except model.DoesNotExist:
            return False


class DownloadData(View):
    def get(self, request):
        try:
            year = int(str(self.request.GET.get("year", None)))
            download_esports_files()
            download_games(year)
            return {"message": "save correctly", "success": True}

        except Exception as e:
            print(str(e))
            return Http404({"message": "Wasn't save correctly", "success": False})
