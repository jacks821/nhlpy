class Team:
    def __init__(self, team, roster):
        self.id = team['id']
        self.name = team['name']
        self.link = team['link']
        self.venue = Venue(team['venue'])
        self.abbrev = team['abbreviation']
        self.teamname = team['teamName']
        self.location = team['locationName']
        self.firstYear = team['firstYearOfPlay']
        self.division = Division(team['division'])
        self.conference = Conference(team['conference'])
        self.franchise = Franchise(team['franchise'])
        self.shortName = team['shortName']
        self.url = team['officialSiteUrl']
        self.franchiseId = team['franchiseId']
        self.active = team['active']
        self.roster = roster

class Timezone:
    def __init__(self, tz):
        self.id = tz['id']
        self.offset = tz['offset']
        self.tz = tz['tz']

class Venue:
    def __init__(self, venue):
        self.id = venue['id']
        self.name = venue['name']
        self.link = venue['link']
        self.city = venue['city']
        self.timezone = Timezone(venue['timeZone'])


class Division:
    def __init__(self, division):
        self.id = division['id']
        self.name = division['name']
        self.nameShort = division['nameShort']
        self.link = division['link']
        self.abv = division['abbreviation']


class Conference:
    def __init__(self, conference):
        self.id = conference['id']
        self.name = conference['name']
        self.link = conference['link']

class Franchise:
    def __init__(self, franchise):
        self.franchiseId = franchise['franchiseId']
        self.teamName = franchise['teamName']
        self.link = franchise['link']
