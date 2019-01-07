import requests
import json



def request(url):
    base = "https://statsapi.web.nhl.com/"
    reqUrl = base + url
    r = requests.get(reqUrl)
    return json.loads(r.content)

def findPlayer(playerName):
    url = "api/v1/teams/?expand=team.roster"
    teams = request(url)['teams']
    for team in teams:
        roster = team['roster']['roster']
        for player in roster:
            if playerName == player['person']['fullName']:
                return request(player['person']['link'])['people'][0]
    return "Could not find player"


#Gets player stats for given season.
#Assumes that the year given is the latter calendar year in the season.
def getPlayerSeasonStats(playerName, season):
    player = findPlayer(playerName)
    s1 = season - 1
    req = player['link'] + "/stats" + "?stats=statsSingleSeason&season=" + str(s1) + str(season)
    return request(req)['stats'][0]
            
    
    
    
