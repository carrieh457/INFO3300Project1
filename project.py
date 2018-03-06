import json
import requests

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}

teamIDs = []

for i in range(1610612737, 1610612766):
	teamIDs += [i]

playerIDs = []

players1 = []

for teamID in teamIDs:
	url1 = 'http://stats.nba.com/stats/commonteamroster/?'
	params1 = dict(
		Season="2006-07",
		TeamID=teamID
	)
	response = requests.get(url=url1, params=params1, headers=headers)
	print(response.json()['resultSets'][0]['rowSet'])
	players1 += response.json()['resultSets'][0]['rowSet']


for player in players1:
	playerIDs += [player[len(player) - 1]]

url = 'http://stats.nba.com/stats/shotchartdetail?'

params = dict(
    Period=0,
    VsConference="",
    LeagueID="00",
    LastNGames=0,
    TeamID=0,
    OpponentTeamID=0,
    Position="",
    Location="",
    Outcome="",
    DateFrom="",
    StartPeriod="",
    DateTo="",
    ContextFitler="",
    RangeType="",
    AheadBehind="",
    EndRange="",
    VsDivision="",
    SeasonSegment="",
    GameSegment="",
    RookieYear="",
    GameID="",
    ContextMeasure="FGA",
    Season="2006-07",
    PlayerID=playerIDs[0],
    Month=0,
    SeasonType="Regular Season",
    PlayerPosition=""
)

makebins = []
attemptbins = []

for x in range(0,50):
	makebins.append([])
	attemptbins.append([])
	for y in range(0, 47):
		makebins[x].append(0)
		attemptbins[x].append(0)

for playerID in playerIDs:
	params['PlayerID'] = playerID
	response = requests.get(url=url, params=params, headers=headers)
	shots = response.json()['resultSets'][0]['rowSet']

	print(playerID)
	if bool(shots):
		print(shots[0][4])

	for shot in shots:
		x = shot[17]
		y = shot[18]
		made = shot[20]
		if shot[12] == "3PT Field Goal":
			made *= 1.5
		if (y < 422.5):
			attemptbins[int((249.99-x)/10)][int((y+47.5)/10)] += 1
			makebins[int((249.99-x)/10)][int((y+47.5)/10)] += made

print(makebins)
print(attemptbins)

		
