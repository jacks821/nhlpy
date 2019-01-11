import requests
import json
from team import Team
from player import Player
from request import getPlayerSeasonStats, getPlayerMonthlySplit, getPlayerWinLossSplit, getPlayerDailySplit, getPlayerVsConference, getPlayerVsDivision, getPlayerVsTeam, getPlayerStatRanks, findTeam, getSchedule

r = getSchedule(team="Nashville Predators")
print(r)



