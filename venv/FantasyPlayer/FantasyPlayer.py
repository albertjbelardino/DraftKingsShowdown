class FantasyPlayer():
    def __init__(self, formatted_stats):
        self.points = 0
        self.position = ''
        self.scoringType = DraftKingsShowdown().createPlayer(formatted_stats)