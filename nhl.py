import requests
import json
from team import Team
from player import Player
from request import getPlayerSeasonStats

y = getPlayerSeasonStats("Alex Tuch", 2018)

print(y)

