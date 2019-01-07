class Player:
    def __init__(self, player):
        self.id = player['id']
        self.fullName = player['fullName']
        self.link = player['link']
        self.num = player['primaryNumber']
        self.birthDate = player['birthDate']
        self.currentAge = player['currentAge']
        self.birthCity = player['birthCity']
        self.birthCountry = player['birthCountry']
        self.nationality = player['nationality']
        self.height = player['height']
        self.weight = player['weight']
        self.active = player['active']
        self.alternateCaptain = player['alternateCaptain']
        self.captain = player['captain']
        self.rookie = player['rookie']
        self.shootsCatches = player['shootsCatches']
        self.rosterStatus = player['rosterStatus']
        self.currentTeam = player['currentTeam']['id']
        self.position = player['primaryPosition']['name']