class FantasyPlayer():
    def __init__(self, player):
        self.scoringType = DraftKingsShowdown()
        self.points = scoringType.createPlayer(player)
        self.position = ''
