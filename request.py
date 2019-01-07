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


#Gets player stats for given season, with the options available.
#Assumes that the year given is the latter calendar year in the season.
#Not meant to be publicly consumed as it assumes that only one of the options will be checked.
def getPlayerSeasonStatswOpts(playerName, season, splits=False, wl=False, monthly=False, daily=False, division=False, conf=False, team=False, game=False, rank=False):
    player = findPlayer(playerName)
    s1 = season - 1
    if wl == True:
        req = player['link'] + "/stats" + "?stats=winLoss&season=" + str(s1) + str(season)
        return request(req)['stats'][0]['splits']
    if splits == True:
        req = req = player['link'] + "/stats" + "?stats=homeAndAway&season=" + str(s1) + str(season)
        return request(req)['stats'][0]['splits']
    if monthly == True:
        req = req = player['link'] + "/stats" + "?stats=byMonth&season=" + str(s1) + str(season)
        return request(req)['stats'][0]['splits']
    if daily == True:
        req = req = player['link'] + "/stats" + "?stats=byDayOfWeek&season=" + str(s1) + str(season)
        return request(req)['stats'][0]['splits']
    if division == True:
        req = req = player['link'] + "/stats" + "?stats=vsDivision&season=" + str(s1) + str(season)
        return request(req)['stats'][0]['splits']
    if conf == True:
        req = req = player['link'] + "/stats" + "?stats=vsConference&season=" + str(s1) + str(season)
        return request(req)['stats'][0]['splits']
    if team == True:
        req = req = player['link'] + "/stats" + "?stats=vsTeam&season=" + str(s1) + str(season)
        return request(req)['stats'][0]['splits']
    if game == True:
        req = req = player['link'] + "/stats" + "?stats=gameLog&season=" + str(s1) + str(season)
        return request(req)['stats'][0]['splits']
    if rank == True:
        req = req = player['link'] + "/stats" + "?stats=regularSeasonStatRankings&season=" + str(s1) + str(season)
        return request(req)['stats'][0]['splits']
    req = player['link'] + "/stats" + "?stats=statsSingleSeason&season=" + str(s1) + str(season)
    return request(req)['stats'][0]


def getPlayerSeasonStats(playerName, season):
    return getPlayerSeasonStatswOpts(playerName, season)

def getPlayerHomeAwaySplit(playerName, season):
    return getPlayerSeasonStatswOpts(playerName, season, splits=True)

def getPlayerMonthlySplit(playerName, season):
    return getPlayerSeasonStatswOpts(playerName, season, monthly=True)

def getPlayerVsTeam(playerName, season):
    return getPlayerSeasonStatswOpts(playerName, season, team=True)

def getPlayerVsConference(playerName, season):
    return getPlayerSeasonStatswOpts(playerName, season, conf=True)

def getPlayerVsDivision(playerName, season):
    return getPlayerSeasonStatswOpts(playerName, season, division=True)

def getPlayerStatRanks(playerName, season):
    return getPlayerSeasonStatswOpts(playerName, season, rank=True)

def getPlayerDailySplit(playerName, season):
    return getPlayerSeasonStatswOpts(playerName, season, daily=True)

def getPlayerWinLossSplit(playerName, season):
    return getPlayerSeasonStatswOpts(playerName, season, wl=True)

    
    
    
