import csv, json
from .models import League, Tournament, Team, Player, Game, GameDetail
from django.http import HttpResponse, JsonResponse
from django.views import View


# Create your views here.
def index(request):
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
            # modelRow.id
            # modelRow.save()
        # m = League(reader)
        # m.save()
    return HttpResponse("Hello world")


def getAllLeagues(request):
    result = League.objects.all()
    return HttpResponse(result)


def SetTournaments(request):
    filePath = "/home/yonathancruz/Descargas/tournaments-json.csv"
    with open(filePath) as f:
        reader = csv.DictReader(f)
        for index, row in enumerate(reader):
            index = index + 1
            modelRow = Tournament()
            modelRow.id = index
            modelRow.idLeague = row["leagueId"]
            modelRow.name = row["name"]
            modelRow.slug = row["slug"]
            modelRow.sport = row["sport"]
            modelRow.startDate = row["startDate"]
            modelRow.endDate = row["endDate"]
            modelRow.save_base()

    return HttpResponse("Data saved in Tournament table")


def SetTeams(request):
    filePath = "/home/yonathancruz/Descargas/teams-json.csv"
    with open(filePath) as f:
        reader = csv.DictReader(f)
        for index, row in enumerate(reader):
            index = index + 1
            modelRow = Team()
            modelRow.id = index
            modelRow.idTeam = row["team_id"]
            modelRow.name = row["name"]
            modelRow.acronym = row["acronym"]
            modelRow.slug = row["slug"]
            modelRow.save_base()

    return HttpResponse("Data saved in Teams table")


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


def SetPlayersJson(request):
    filePath = "/home/yonathancruz/bckPowerRankingLol/data/2023 game incomplete/esports-data/players.json"

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
        participantsCounter = 0
        try:
            filePath = "/home/yonathancruz/bckPowerRankingLol/data/2021 game incomplete/esports-data/mapping_data.json"
            with open(filePath) as f:
                reader = json.load(f)

                for gameNumber, row in enumerate(reader):
                    gameNumber += 1
                    gameId = int(float(row["esportsGameId"]))
                    queryGame = self.get_object(Game, gameId)
                    if queryGame:
                        if gameNumber > 25278:
                            listParticipants = row["participantMapping"]
                            # verify if a the list of participants is equal to 10
                            if len(listParticipants) == 10:
                                playersFounded = []
                                for player in listParticipants:
                                    participantsCounter += 1
                                    # Get Player Id
                                    idPlayer = int(float(listParticipants[player])) if type(listParticipants[player]) == type(1) else 0

                                    # @dev verify if a value is a number after search
                                    if type(idPlayer) == type(1):
                                        queryPlayer = self.get_object(Player, idPlayer)
                                        print("PLayer exits", queryPlayer)
                                        # if player does not exits in table player skip the current participants list loop
                                        playerMatch = True

                                        if not queryPlayer:
                                            playerMatch = False

                                        playersFounded.append(
                                            {
                                                "queryset": queryGame,
                                                "idPlayer": queryPlayer,
                                                "playerMatch": playerMatch,
                                            }
                                        )

                                # @dev if participants is not equal to 10 skip current game loop
                                if participantsCounter == 10:
                                    # if not save the current game lop into detail
                                    for value in playersFounded:
                                        print("Game: ",gameNumber, "\nPlayers Info: ", value)
                                        modelRow = GameDetail(
                                            idGameDetail=gameNumber,
                                            idGame=value["queryset"],
                                            idPlayer=value["idPlayer"],
                                            playerMatch=value["playerMatch"],
                                        )
                                        modelRow.save_base()
                                    participantsCounter = 0
                                else:
                                    print("\nGame not equal to 10: ", participantsCounter)

        except Exception as e:
            print("\nError: ")
            print(e)
            return JsonResponse({"Error": str(e)})
        return JsonResponse({"info": "Data saved correctly"})

    def get_object(self, querySet, id):
        print(id)
        try:
            return querySet.objects.get(pk=id)
        except querySet.DoesNotExist:
            return False
