import sys
sys.path.append('C:\\Users\\tug83326\\PycharmProjects\\DraftKingsShowdown\\venv\\Lib\\site-packages')
sys.path.append('C:\\Users\\tug83326\\PycharmProjects\\DraftKingsShowdown\\venv\\ScoringType')
sys.path.append('C:\\Users\\tug83326\\PycharmProjects\\DraftKingsShowdown\\venv\\FantasyPlayer')
import nflgame


class DraftKingsShowdown():
    def __init__(self):
        self.x = 0.0

    def calculateReceiving(self, receiving_yds, receiving_tds, receptions):
        receiving_pts = 0.0
        receiving_pts += receiving_yds / 10.0
        receiving_pts += receptions
        receiving_pts += receiving_tds * 6.0
        if receiving_yds >= 100.0:
            receiving_pts += 3.0
        return receiving_pts

    def calculatePassing(self, passing_yds, passing_tds, interceptions):
        passing_pts = 0.0
        passing_pts += passing_yds / 25.0
        passing_pts -= interceptions * 2.0
        passing_pts += passing_tds * 4.0
        if passing_yds >= 300.0:
            passing_pts += 3.0
        return passing_pts

    def calculateKicking(self, kicks_made, kicks_attempted, pats):
        #TODO get actual yardage of kicks
        kicking_pts = 0.0
        kicking_pts += pats
        kicking_pts += kicks_made * 3.0
        kicking_pts -= kicks_attempted
        return kicking_pts

    def calculateRushing(self, rushing_yds, rushing_tds):
        rushing_pts = 0.0
        rushing_pts += rushing_yds / 10.0
        rushing_pts += rushing_tds * 6.0
        if rushing_yds >= 100.0:
            rushing_pts += 3.0
        return rushing_pts

    def createPlayer(self, player):
        player_pts = 0.0
        player_pts += self.calculateRushing(rushing_yds=player.rushing_yds, rushing_tds=player.rushing_tds)
        player_pts += self.calculateReceiving(receiving_yds=player.receiving_yds, receiving_tds=player.receiving_tds,
                                              receptions=player.receiving_rec)
        player_pts += self.calculatePassing(passing_yds=player.passing_yds, passing_tds=player.passing_tds,
                                            interceptions=player.passing_ints)
        return player_pts

class FantasyPlayer():

    scoringType = DraftKingsShowdown()
    points = 0.0

    def __init__(self, player):
        self.player = player
        self.points = self.getPoints()
        self.team = player.team
        self.position = player.guess_position

    def getPoints(self):
        return self.scoringType.createPlayer(self.player)

def isCloseEnough(homeScore, awayScore, line, ou):
    if ou + 5 > homeScore + awayScore > ou - 5:
        if line + 5 > homeScore - awayScore > line - 5:
            return True
    return False

class PlayerDistribution():

    def __init__(self):
        self.distro_dict = {
            'home_rb' : 0,
            'home_qb' : 0,
            'home_te' : 0,
            'home_wr' : 0,
            'away_rb' : 0,
            'away_qb' : 0,
            'away_te' : 0,
            'away_wr' : 0
        }




def getGameByEid(eid):
    return nflgame.game.Game(eid)

def displayPointTotalsByYearAndWeek(year, week):
    list_fplayers = []

    games = nflgame.games(2018, week=1)
    players = nflgame.combine_game_stats(games)
    for p in players:
        my_fplayer = FantasyPlayer(p)
        list_fplayers.append(my_fplayer)

    newlist = sorted(list_fplayers, key=lambda x: x.points)

    for fplayer in newlist:
        msg = '%s %3.2f'
        print msg % (fplayer.player, fplayer.points)

def displayPointTotalsByGame(eid):
    list_fplayers = []

    game = getGameByEid(eid)
    players = game.players

    print(game.nice_score())
    for p in players:
        my_fplayer = FantasyPlayer(p)
        list_fplayers.append(my_fplayer)

    newlist = sorted(list_fplayers, key=lambda x: x.points, reverse=True)

    for fplayer in newlist[0:2]:
        msg = '%s %3.2f'
        print msg % (fplayer.player, fplayer.points)

    return newlist

def getPlayerType(player, game):
    if player.position == 'QB' and player.team == game.home:
        return 'home_qb'
    if player.position == 'RB' and player.team == game.home:
        return 'home_rb'
    if player.position == 'TE' and player.team == game.home:
        return 'home_te'
    if player.position == 'WR' and player.team == game.home:
        return 'home_wr'
    if player.position == 'QB' and player.team == game.away:
        return 'away_qb'
    if player.position == 'RB' and player.team == game.away:
        return 'away_rb'
    if player.position == 'TE' and player.team == game.away:
        return 'away_te'
    if player.position == 'WR' and player.team == game.away:
        return 'away_wr'

def displayPointTotalsByVegas(line, ou):
    start = 2016
    end = 2018

    weeks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]

    first_place_distro = PlayerDistribution()
    second_place_distro = PlayerDistribution()
    #third_place_distro = PlayerDistribution()
    my_game_ids = []

    for i in range(start, end):
        games = nflgame.games(i, week=weeks)
        for game in games:
            if isCloseEnough(homeScore=game.score_home, awayScore=game.score_away, line=line, ou=ou):
                player_list = displayPointTotalsByGame(game.eid)
                val = getPlayerType(player_list[0], game)
                print(val)
                if val is not None:
                    first_place_distro.distro_dict[val] += 1
                #first_place_distro.distro_dict[getPlayerType(player_list[0], game)] += 1
                second_place_distro.distro_dict[getPlayerType(player_list[1], game)] += 1
                #third_place_distro.distro_dict[getPlayerType(player_list[2], game)] += 1
                my_game_ids.append(game.eid)

    print(first_place_distro.distro_dict)
    print(second_place_distro.distro_dict)
    #print(third_place_distro.distro_dict)

#displayPointTotalsByYearAndWeek(2018, 1)
displayPointTotalsByVegas(3, 57)

