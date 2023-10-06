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
from django.http import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.db import transaction


def index(request):
    return HttpResponse("Hello World")


# Create your views here.
@transaction.atomic
def SetLeague(request):
    urlCsv = "/home/yonathancruz/Descargas/leagues-json.csv"
    with open(urlCsv) as f:
        reader = csv.DictReader(f)
        for index, row in enumerate(reader):
            index = index + 1
            modelRow = League()
            modelRow.id = index
            modelRow.idLeague = row["idLeague"]
            modelRow.name = row["name"]
            modelRow.slug = row["slug"]
            modelRow.sport = row["sport"]
            modelRow.image = row["image"]
            modelRow.lightImage = row["lightImage"]
            modelRow.darkImage = row["darkImage"]
            modelRow.region = row["region"]
            modelRow.priority = row["priority"]
            modelRow.displayPriorityPosition = row["displayPriorityPosition"]
            modelRow.displayPriorityStatus = (
                True if row["displayPriorityStatus"] == "selected" else False
            )
            modelRow.save_base()
    return HttpResponse("Hello world")


@transaction.atomic
def getAllLeagues(request):
    result = League.objects.all()
    return HttpResponse(result)


@transaction.atomic
def SetTournaments(request):
    filePath = "/home/yonathancruz/Descargas/tournaments-json.csv"
    with open(filePath) as f:
        reader = csv.DictReader(f)
        for index, row in enumerate(reader):
            print(row)
            index = index + 1
            modelRow = Tournament()
            modelRow.idTournament = row["id"]
            modelRow.idLeague = row["leagueId"]
            modelRow.name = row["name"]
            modelRow.slug = row["slug"]
            modelRow.sport = row["sport"]
            modelRow.startDate = row["startDate"]
            modelRow.endDate = row["endDate"]
            modelRow.save_base()

    return HttpResponse("Data saved in Tournament table")


@transaction.atomic
def SetTeams(request, year):
    filePath = (
        "/home/yonathancruz/data/"
        + str(year)
        + " game incomplete/esports-data/teams.json"
    )
    with open(filePath) as f:
        reader = json.load(f)
        for index, row in enumerate(reader):
            index += 1
            modelRow = Team()
            modelRow.idTeam = row["team_id"]
            modelRow.name = row["name"]
            modelRow.acronym = row["acronym"]
            modelRow.slug = row["slug"]
            modelRow.save_base()

    return HttpResponse("Data saved in Teams table")


@transaction.atomic
def SetPlayers(request):
    filePath = "/home/yonathancruz/Descargas/players-json.csv"
    with open(filePath) as f:
        reader = csv.DictReader(f)
        for row in reader:
            modelRow = Player()
            modelRow.idPlayer = row["idPlayer"]
            modelRow.idTeam = row["idTeam"] if (len(str(row["idTeam"])) > 0) else None
            modelRow.handle = row["handle"]
            modelRow.name = str(row["first_name"] + " " + row["last_name"])
            modelRow.save_base()

    return HttpResponse("Data saved in PLayers table")


@transaction.atomic
def SetPlayersJson(request):
    filePath = "/home/yonathancruz/data/2021 game incomplete/esports-data/players.json"

    with open(filePath) as f:
        reader = json.load(f)
        for row in reader:
            if row["home_team_id"]:
                model = Player(
                    idPlayer=row["player_id"],
                    idTeam=row["home_team_id"],
                    handle=row["handle"],
                    name=row["first_name"] + " " + row["last_name"],
                )
                model.save_base()

    return HttpResponse("Data saved in PLayers table")


@transaction.atomic
def SetGameInfo(request):
    filePath = "/home/yonathancruz/Descargas/gameInfo-json.csv"
    with open(filePath) as f:
        reader = csv.DictReader(f)
        for index, row in enumerate(reader):
            index = index + 1
            if index > 20000:
                modelRow = Game()
                modelRow.idGame = row["idGame"]
                modelRow.idPlatform = row["idPlatform"]
                modelRow.save_base()

    return HttpResponse("Data saved in Game table")


class SetGameDetail(View):
    Game = Game

    def get(self, resquest):
        try:
            with transaction.atomic():
                filePath = "/home/yonathancruz/data/2023 game incomplete/esports-data/mapping_data.json"
                with open(filePath) as f:
                    reader = json.load(f)
                    # READ the json file
                    for gameNumber, row in enumerate(reader):
                        gameNumber += 1
                        gameId = row["esportsGameId"]
                        queryGame = self.get_object(gameId, "Game")
                        if queryGame:
                            if gameNumber < 40000:
                                listParticipants = row["participantMapping"]
                                print("Participants: ", listParticipants)
                                # verify if a the list of participants is equal to 10
                                if len(listParticipants) == 10:
                                    # get game instance to save in db
                                    result = self.get_game_detail_or_false(
                                        queryGame, listParticipants
                                    )

                                    # save to db
                                    result.save_base()

                                else:
                                    print(
                                        "\nPlayer list isn't complete, quit current player list"
                                    )
                        else:
                            HttpResponse(404, "Game not found")
        except Exception as e:
            print(e)
            return HttpResponse(str(e))
        return HttpResponse("Data saved correctly")

    def get_game_detail_or_false(self, gameInstance, listPlayers):
        playersFounded = []
        for playerCounter, player in enumerate(listPlayers):
            playerCounter += 1
            # Get Player Id
            idPlayer = listPlayers[player]
            queryPlayer = self.get_object(idPlayer, "Player")
            print("Player record #", playerCounter, "Player query: ", queryPlayer)
            if queryPlayer:
                playerMatch = True
                gameDetail = {"idPlayer": idPlayer, "playerMatch": playerMatch}
                playersFounded.append(gameDetail)
            else:
                playerMatch = False
                gameDetail = {"idPlayer": idPlayer, "playerMatch": playerMatch}
                playersFounded.append(gameDetail)

        # @dev if participants is not equal to 10 skip current game loop
        if len(playersFounded) == 10:
            # if not save the current game lop into detail
            for playerInstance in playersFounded:
                gameDetailInstace = GameDetail(
                    idGame=gameInstance,
                    idPlayer=playerInstance["idPlayer"],
                    playerMatch=playerInstance["playerMatch"],
                )
                playersFounded.clear()
                return gameDetailInstace
            else:
                print(len(playersFounded))
                playersFounded.clear()
                HttpResponse(404, "\nGame not equal to 10")

    def get_object(self, id, modelName):
        try:
            if modelName == "Game":
                try:
                    query = Game.objects.get(pk=id)
                except Game.DoesNotExist:
                    return False

                if query:
                    return Game(
                        idGame=query.idGame,
                        idPlatform=query.idPlatform,
                        year=query.year,
                    )
                else:
                    return False

            if modelName == "Player":
                try:
                    query = Player.objects.get(pk=id)
                except Player.DoesNotExist:
                    return False

                if query:
                    return Player(
                        idPlayer=query.idPlayer,
                        idTeam=query.idTeam,
                        handle=query.handle,
                        name=query.name,
                    )
                else:
                    return False

        except Exception as e:
            print("Ocurrio un error: ", e)
            return False


# reading game json file
def openGameJson(request, year, game, item):
    filePath = (
        "/home/yonathancruz/data/"
        + str(year)
        + "_game_incomplete/games/"
        + game
        + ".json"
    )
    print(filePath)
    with open(filePath) as f:
        reader = json.load(f)
        for index, row in enumerate(reader):
            index = index + 1
            if index == item:
                return JsonResponse(row)


# save the stages from tournaments data
@method_decorator(transaction.atomic, name="dispatch")
class SetStagesAndSection(View):
    def get(self, request):
        try:
            filePath = "/home/yonathancruz/data/2023 game incomplete/esports-data/tournaments.json"
            with open(filePath) as f:
                tournaments = json.load(f)
                for index, tournament in enumerate(tournaments):
                    index += 1
                    queryset = self.get_object_or_false(
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
                            model.idTournament = queryset
                            model.name = stage["name"]
                            model.type = stage["type"]
                            model.slug = stage["slug"]
                            model.save_base()
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
                                    idStage=model, name=section["name"]
                                )

                                modelSection.save_base()

                                ################
                                ## save match ##
                                ################

                                matches = section["matches"]
                                for match in matches:
                                    modelMatch = Match(
                                        idSection=modelSection,
                                        type=match["type"],
                                        state=match["state"],
                                        mode=match["mode"],
                                        strategy=match["strategy"]["type"]
                                        + " "
                                        + str(match["strategy"]["count"]),
                                    )
                                    modelMatch.save_base()

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
                                                "\nSkip curret detail => idTeam #:"
                                                + team["id"]
                                            )
                                        else:
                                            modelMatchDetail = MatchDetail(
                                                idMatch=modelMatch,
                                                idTeam=queryTeam,
                                                matchTeamIntegrants=matchPlayers,
                                                win=False
                                                if team["result"]["outcome"] == "loss"
                                                else True,
                                            )
                                            modelMatchDetail.save_base()
            return JsonResponse(
                {"message": "Your information was save correctly", "success": True}
            )
        except Exception as e:
            print("ERROR: ", str(e))
            return JsonResponse({"message": "Wasn't save correctly", "success": False})

    def get_object_or_false(self, key, model, type):
        try:
            if type == "primaryKey":
                return model.objects.get(pk=key)
            if type == "lastField":
                return model.objects.last()
            else:
                return model.objects.get(name=key)
        except model.DoesNotExist:
            return False

    def participants_match_or_false(self, listIntegrants):
        listMatches = []
        try:
            for integrant in listIntegrants:
                print("Verifying player #: ", integrant["id"])
                response = Player.objects.get(pk=integrant["id"])
                listMatches.append(response)

            if False in listMatches:
                return False
            else:
                return True
        except Exception as e:
            return False
