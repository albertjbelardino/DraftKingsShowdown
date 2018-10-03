import sys
sys.path.append('C:\\Users\\tug83326\\PycharmProjects\\DraftKingsShowdown\\venv\\Lib\\site-packages')
import nflgame

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