class DraftKingsShowdown:
    def __init__(self):
        pass

    def calculateReceiving(self, receiving_yds, receiving_tds):
        receiving_pts = 0
        receiving_pts += receiving_yds / 10
        receiving_pts += receptions
        receiving_pts += receiving_tds * 6
        if receiving_yds >= 100:
            receiving_pts += 3
        return receiving_pts

    def calculatePassing(self, passing_yds, passing_tds):
        passing_pts = 0
        passing_pts += passing_yds / 25
        passing_pts -= interceptions * 2
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
