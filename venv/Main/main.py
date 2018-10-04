import sys
sys.path.append('C:\\Users\\tug83326\\PycharmProjects\\DraftKingsShowdown\\venv\\Lib\\site-packages')
sys.path.append('C:\\Users\\tug83326\\PycharmProjects\\DraftKingsShowdown\\venv\\ScoringType')
sys.path.append('C:\\Users\\tug83326\\PycharmProjects\\DraftKingsShowdown\\venv\\FantasyPlayer')
import nflgame


class DraftKingsShowdown():
    def __init__(self):
        self.x = 0

    def calculateReceiving(self, receiving_yds, receiving_tds):
        receiving_pts = 0
        receiving_pts += receiving_yds / 10
        #receiving_pts += receptions
        receiving_pts += receiving_tds * 6
        if receiving_yds >= 100:
            receiving_pts += 3
        return receiving_pts

    def calculatePassing(self, passing_yds, passing_tds):
        passing_pts = 0
        passing_pts += passing_yds / 25
        #passing_pts -= interceptions * 2
        passing_pts += passing_tds * 4
        if passing_yds >= 300:
            passing_pts += 3
        return passing_pts

    def calculateKicking(self, kicks_made, kicks_attempted, pats):
        #TODO get actual yardage of kicks
        kicking_pts = 0
        kicking_pts += pats
        kicking_pts += kicks_made * 3
        kicking_pts -= kicks_attempted
        return kicking_pts

    def calculateRushing(self, rushing_yds, rushing_tds):
        rushing_pts = 0
        rushing_pts += rushing_yds / 10
        rushing_pts += rushing_tds * 6
        if rushing_yds >= 100:
            rushing_pts += 3
        return rushing_pts

    def createPlayer(self, player):
        player_pts = 0
        player_pts += self.calculateRushing(rushing_yds=player.rushing_yds, rushing_tds=player.rushing_tds)
        player_pts += self.calculateReceiving(receiving_yds=player.receiving_yds, receiving_tds=player.receiving_tds)
        player_pts += self.calculatePassing(passing_yds=player.passing_yds, passing_tds=player.passing_tds)
        return player_pts

class FantasyPlayer():

    scoringType = DraftKingsShowdown()
    points = 0.0

    def __init__(self, player):
        self.player = player
        self.points = self.getPoints()
        self.position = ''

    def getPoints(self):
        return self.scoringType.createPlayer(self.player)

def isCloseEnough(homeScore, awayScore, line, ou):
    if ou + 5 > homeScore + awayScore > ou - 5:
        if line + 5 > homeScore - awayScore > line - 5:
            return True
    return False

def getGameByEid(eid):
    return nflgame.game.Game(id)

my_game_ids = []

games = nflgame.games(2013, week=[1,2,3,4,5,6,7])
for game in games:
    if isCloseEnough(homeScore=game.score_home, awayScore=game.score_away, line=10, ou=51):
        my_game_ids.append(game.eid)
for id in my_game_ids:
    print '%s' % getGameByEid(id).home
stats = nflgame.combine_game_stats(games)
for s in stats.sort('passing_yds').limit(5):
    msg = '%s %d'
    print msg % (s, s.passing_yds)

list_fplayers = []

games = nflgame.games(2018, week=1)
players = nflgame.combine_game_stats(games)
for p in players:
    my_fplayer = FantasyPlayer(p)
    list_fplayers.append(my_fplayer)

newlist = sorted(list_fplayers, key=lambda x: FantasyPlayer.points)

for fplayer in newlist:
    msg = '%s %d'
    print msg % (fplayer.player, fplayer.points)