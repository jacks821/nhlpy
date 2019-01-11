import requests
import json
from team import Team
from player import Player
from request import getTeamStats, _getStandings, getPlayerSeasonStats, getPlayerMonthlySplit, getPlayerWinLossSplit, getPlayerDailySplit, getPlayerVsConference, getPlayerVsDivision, getPlayerVsTeam, getPlayerStatRanks, findTeam, getSchedule

r = getTeamStats("Vegas Golden Knights")
print(r)
