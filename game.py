__author__ = 'usucuha'

class Game:
    def __init__(self, gameName):
        self.gameName = gameName
        self.currentTurn = 1

        self.companies = [
            "Seattle First National Bank",
            "Rainier National Bank",
            "Weyerhauser Corp.",
            "Georgia-Pacific",
            "Bellevue Square",
            "Northgate Mall",
            "Boeing Aerospace",
            "Pacific Car & Foundry"
        ]

