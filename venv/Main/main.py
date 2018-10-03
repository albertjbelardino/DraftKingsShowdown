import sys
sys.path.append('C:\\Users\\tug83326\\PycharmProjects\\DraftKingsShowdown\\venv\\Lib\\site-packages')
import nflgame

games = nflgame.games(2013, week=1)
plays = nflgame.combine_plays(games)
for p in plays.sort('passing_yds').limit(5):
    print(p)